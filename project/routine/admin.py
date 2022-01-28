from django.contrib import admin
from django.db import models
from datetime import datetime, date

from .models import (WorkoutDailyRoutine, CourseDailyRoutine)
from workout.admin import WorkoutPlanInlineAdmin  # noqa
from core.libs.error_handling import write_in_log  # noqa
from inspect import currentframe, getframeinfo


@admin.register(WorkoutDailyRoutine)
class DailyWorkoutAdmin(admin.ModelAdmin):
    inlines = [WorkoutPlanInlineAdmin]
    search_fields = ['date']
    readonly_fields = ('created', 'updated')
    list_display = ('get_weekday', 'date', 'get_workout_types',
                    'get_nr_workouts', 'get_nr_workouts_todo',
                    'get_nr_done_workouts', 'get_workouts_tot_time',
                    'get_workouts_done_time')
    save_as = True


@admin.register(CourseDailyRoutine)
class DailyCourseAdmin(admin.ModelAdmin):
    # inlines = [WorkoutPlanInlineAdmin]
    search_fields = ['date']
    readonly_fields = ('created', 'updated')
    list_display = ('date', 'created', 'updated')
    save_as = True
