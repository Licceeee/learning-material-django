from django.db import models
from datetime import datetime, date
from django.utils.html import format_html
from django.conf import settings
from core.models import Timestamps
from core.libs.global_functions import calc_min_or_hour

today = date.today()


def _get_weekday(_date):
    if _date == date.today():
        return format_html(
            f'<b style="color: green;">{_date.strftime("%A")}</b>')
    if _date < date.today():
        return format_html(
            f'<b style="color: #BEBEBE;">{_date.strftime("%A")}</b>')
    return _date.strftime("%A")


class WorkoutDailyRoutine(Timestamps):
    date = models.DateField(default=datetime.now, unique=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.date.strftime('%d %B %Y')} - {self.date.strftime('%A')}"

    def get_nr_workouts(self):
        res = self.workoutplan_set.count()
        if res > 0:
            return res
    get_nr_workouts.short_description = "# Total Workouts"

    def get_nr_workouts_todo(self):
        res = self.workoutplan_set.filter(done=False).count()
        if res > 0:
            return res
    get_nr_workouts_todo.short_description = "# Workouts ToDo"

    def get_nr_done_workouts(self):
        res = self.workoutplan_set.filter(done=True).count()
        if res > 0:
            return res
    get_nr_done_workouts.short_description = "# Workouts Done"

    def get_workouts_tot_time(self):
        time = 0
        for plan in self.workoutplan_set.all():
            if plan.workout.time_in_min:
                time += plan.workout.time_in_min
        if time > 0:
            converted_time = calc_min_or_hour(time)
            return converted_time
    get_workouts_tot_time.short_description = "Total Time"

    def get_workouts_done_time(self):
        time = 0
        for plan in self.workoutplan_set.filter(done=True):
            if plan.workout.time_in_min:
                time += plan.workout.time_in_min
        if time > 0:
            converted_time = calc_min_or_hour(time)
            return format_html(f'<b style="color: green">{converted_time}</b>')
    get_workouts_done_time.short_description = "Time Done Workouts"

    def get_weekday(self):
        return _get_weekday(self.date)
    get_weekday.short_description = "Day"

    def get_workout_types(self):
        """Get workout types"""
        workout_types = ""
        for workout_plan in self.workoutplan_set.all():
            for workout_type in workout_plan.workout.types.all():
                if workout_type.name not in workout_types:
                    workout_types += (f'{workout_type.name}<br>')
        return format_html(workout_types)
    get_workout_types.short_description = "Workout Types"


class CourseDailyRoutine(Timestamps):
    date = models.DateField(default=datetime.now, unique=True)

    class Meta:
        ordering = ['-date']
