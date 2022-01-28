from django.shortcuts import render
from datetime import datetime, date, timedelta
import datetime
from isoweek import Week  # noqa
from django.db.models import Q
import pandas  # noqa
from crum import get_current_user

from django.views.generic import (TemplateView)
from routine.models import WorkoutRoutine, Category  # noqa


def get_or_create_routine(date):
    """Returns an existing object or creates a new one if not"""
    obj, created = WorkoutRoutine.objects.get_or_create(date=date)
    if created:
        return created
    return obj


def get_weekly_routines(start_date, end_date):
    """Returns the routines between two dates
        Args: start date
                end date
    """
    for day in pandas.date_range(start_date, end_date):
        get_or_create_routine(day)
    return WorkoutRoutine.objects.filter(
        Q(date__gte=start_date) &
        Q(date__lte=end_date)).order_by('date')


def get_daily_routines(_date):
    """Returns the routines of given date
        Args: date
    """
    return WorkoutRoutine.objects.filter(date=_date).order_by('date')


def get_tot_min_weekly_tasks(routines):
    minutes = 0
    for routine in routines:
        for plan in routine.plan_set.all():
            minutes += plan.task.time_in_min
    return minutes


def get_tot_min_daily_tasks(routine):
    minutes = 0
    try:
        for plan in routine.plan_set.all():
            minutes += plan.task.time_in_min
    except Exception:
        pass  # TODO write in log
    return minutes


def get_min_tasks_by_category(all_routines, category):
    minutes = 0
    nr_tasks = 0
    for routine in all_routines:
        for plan in routine.plan_set.filter(
                task__category__name=category):
            minutes += plan.task.time_in_min
            nr_tasks += 1
    return minutes, nr_tasks


def get_difference(min_current, min_previous):
    """Calculates the difference from current week/day compared
    to previous week/day"""
    increase = min_current - min_previous
    try:
        return round(increase / min_previous * 100, 2)
    except Exception as e:
        if min_current > 0:
            return 100
        return 0


def get_week_stats(routines, previous_week):
    """Returns the categories, sum of invested minuts, amount
    of tasks of the whole week and difference to previous week in %"""
    categories, objs = [], []
    for cat in Category.objects.all():
        if cat.display_in_stats:
            categories.append(cat.name)

    for category in set(categories):
        """get a distinct list of categories"""
        min_previous_week = get_min_tasks_by_category(
            get_weekly_routines(previous_week.monday(),
                                previous_week.sunday()), category)
        minutes, amount = get_min_tasks_by_category(routines, category)
        difference = get_difference(minutes, min_previous_week[0])
        objs.append({'name': category, 'minutes': minutes,
                     'icon': Category.objects.get(name=category).get_icon(),
                     'amount': amount, 'difference': difference})
        """Sort list of dict alphabetically by name"""
        objs = sorted(objs, key=lambda i: i['name'])
    return objs


def _get_previous_day(date_):
    """returns the previous day to given date"""
    date_from_str = datetime.datetime.strptime(date_, '%Y-%m-%d')
    previous_datetime = date_from_str - datetime.timedelta(days=1)
    previous_date = previous_datetime.date()
    return previous_date


def _get_following_day(date_):
    """returns the previous day to given date"""
    date_from_str = datetime.datetime.strptime(date_, '%Y-%m-%d')
    next_datetime = date_from_str + datetime.timedelta(days=1)
    next_date = next_datetime.date()
    return next_date


class WeekOverView(TemplateView):
    template_name = 'routine/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ! IMPORTANT
        """get week_nr from url"""
        selected_week = self.kwargs['week_nr']
        selected_year = self.kwargs['week_year']
        week_ = Week(selected_year, selected_week)
        previous_week = Week(selected_year, selected_week-1)
        weeknumber = week_.week
        routines = get_weekly_routines(week_.monday(), week_.sunday())

        context['selected_week'] = weeknumber
        context['selected_year'] = selected_year
        context['total_h_invested'] = round(
            get_tot_min_weekly_tasks(routines) / 60, 2)
        context['weekly_routines'] = routines
        context['stats'] = get_week_stats(routines, previous_week)

        return context


class TodaysRoutineView(TemplateView):
    template_name = 'routine/day.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _date = self.kwargs['date']
        routine = get_or_create_routine(_date)

        def get_categories(routine):
            res = []
            try:
                for plan in routine.plan_set.all():
                    if plan.task.category not in res:
                        res.append(plan.task.category)
            except Exception:
                pass
            return res
        categories = get_categories(routine)

        context['tot_min'] = round(get_tot_min_daily_tasks(routine) / 60, 2)
        context['previous_day'] = _get_previous_day(_date)
        context['following_day'] = _get_following_day(_date)
        context['routine'] = routine
        context['date'] = _date
        context['categories'] = categories
        return context


class StatsView(TemplateView):
    template_name = 'routine/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
