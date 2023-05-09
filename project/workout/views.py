from django.views.generic import TemplateView
from isoweek import Week  # noqa
import pandas  # noqa
from routine.models import WorkoutDailyRoutine  # noqa
from .models import Workout
from django.db.models import Q
from core.libs.global_functions import calc_min_or_hour  # noqa
from dal import autocomplete  # noqa
from django.db.models import Q  # noqa


def get_or_create_routine(date):
    """Returns an existing object or creates a new one if not

        Args:

            date (date): date

        Returns:

            object: WorkoutDailyRoutine object
    """
    obj, created = WorkoutDailyRoutine.objects.get_or_create(date=date)
    if created:
        return created
    return obj


def get_weekly_routines(start_date, end_date):
    """Returns a list of routines between two dates

    Args:

        start date (date): start date of routines
        end date (date): end date of routines

    Returns:

        list: filtered list of WorkoutDailyRoutine objects
    """
    for day in pandas.date_range(start_date, end_date):
        get_or_create_routine(day)
    return WorkoutDailyRoutine.objects.filter(
        Q(date__gte=start_date) &
        Q(date__lte=end_date)).order_by('date')


def get_min_weekly_workouts(routines, filter_to=None):
    """Return the amount of minutes/hours per given routines (for a week)
        in total or filtered by done or not done

    Args:

        routines (list): list of WorkoutDailyRoutine objs
        filter to (boolean, optional): workoutplan filter that can be True
        or False. Defaults to None.

    Returns:

        int: minutes
        str: time (hour:h or minutes:m)
    """
    minutes = 0
    for routine in routines:
        if filter_to or filter_to is not None:
            for plan in routine.workoutplan_set.filter(done=filter_to):
                minutes += plan.workout.time_in_min
        else:
            for plan in routine.workoutplan_set.all():
                minutes += plan.workout.time_in_min
    return minutes


def get_nr_of_routines(routines, filter_to=None):
    """Returns the number of workouts in set of given routines

        Args:

            routines (list): list of WorkoutDailyRoutine objects
            filter to (boolean, optional): workoutplan filter that can be True
            or False. Defaults to None.

        Returns:

            int: number of routines
    """
    nr = 0
    for routine in routines:
        if filter_to or filter_to is not None:
            for plan in routine.workoutplan_set.filter(done=filter_to):
                nr += 1
        else:
            for plan in routine.workoutplan_set.all():
                nr += 1
    return nr


def get_diff_min_to_prev_week(min_current, min_previous):
    """Calculates the difference in percentage from current week:day compared
        to a previous week:day

        Args:

            min current (float): sum of minutes of current period of time
            min previous (float): sum of minutes of previous period of time

        Returns:

            int: difference in %
    """
    increase = min_current - min_previous
    try:
        return round(increase / min_previous * 100, 2)
    except Exception:
        if min_current > 0:
            return 100
        return 0


class WorkoutView(TemplateView):
    template_name = 'workout/workout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ! IMPORTANT
        """get week_nr from url"""
        _selected_week = self.kwargs['week_nr']
        _selected_year = self.kwargs['week_year']
        _week = Week(_selected_year, _selected_week)
        _previous_week = Week(_selected_year, _selected_week-1)
        weeknumber = _week.week
        routines = get_weekly_routines(_week.monday(), _week.sunday())
        _routines_prev_week = get_weekly_routines(_previous_week.monday(),
                                                  _previous_week.sunday())

        _min_workouts = get_min_weekly_workouts(routines)
        _min_workouts_done = get_min_weekly_workouts(routines, True)
        _min_workouts_todo = get_min_weekly_workouts(routines, False)

        _min_workouts_prev_week = get_min_weekly_workouts(
            _routines_prev_week)

        context['selected_week'] = weeknumber
        context['selected_year'] = _selected_year
        context['weekly_routines'] = routines

        context['tot_h'] = calc_min_or_hour(_min_workouts)
        context['tot_h_done'] = calc_min_or_hour(_min_workouts_done)
        context['tot_h_to_todo'] = calc_min_or_hour(_min_workouts_todo)
        context['nr_workouts'] = get_nr_of_routines(routines)
        context['nr_workouts_done'] = get_nr_of_routines(routines, True)
        context['nr_workouts_todo'] = get_nr_of_routines(routines, False)
        context['diff_to_prev_week'] = get_diff_min_to_prev_week(
            _min_workouts, _min_workouts_prev_week)

        return context


class WorkoutAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Workout.objects.all()

        if self.q:
            qs = qs.filter(
                Q(types__name__icontains=self.q) |
                Q(name__icontains=self.q)
            )

        return qs
