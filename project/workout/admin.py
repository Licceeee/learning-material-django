from django.contrib import admin
from django.db import models
from datetime import datetime
from .models import (WorkoutType, Workout, WorkoutPlan, Source,
                     DistanceActivity, BodyMeasurement)
from .forms import WorkoutPlanForm
from core.libs.error_handling import write_in_log  # noqa
from inspect import currentframe, getframeinfo
from admin_auto_filters.filters import AutocompleteFilter  # noqa
from adminsortable2.admin import SortableInlineAdminMixin  # noqa


# ===================================================== >> AUTOCOMPLETE FILTERS
class SourceFilter(AutocompleteFilter):
    title = 'Source'  # display title
    field_name = 'source'  # name of the foreign/M2M key field


class WorkoutTypeFilter(AutocompleteFilter):
    title = 'WorkoutType'
    field_name = 'types'


# ================================================================== >> INLINES
class WorkoutPlanInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = WorkoutPlan
    form = WorkoutPlanForm
    extra = 1

    def get_readonly_fields(self, request, obj):
        """Set done readonly for future dates"""
        today = datetime.today().date()
        try:
            if obj and obj.date > today:
                return ('done',)
            else:
                return ()
        except Exception:
            return ()


# ============================================================= >> ADMIN MODELS
@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    search_fields = ['workout__name', 'date']
    autocomplete_fields = ['workout', 'date']
    list_display = ('workout', 'date', 'get_workout_time',
                    'get_workout_done_time', 'done')

    def get_readonly_fields(self, request, obj):
        """Set done readonly for future dates"""
        today = datetime.today().date()
        try:
            if obj.day.date > today:
                return ('created', 'updated', 'done', )
            else:
                return ('created', 'updated')
        except Exception as e:
            frame = getframeinfo(currentframe())
            write_in_log((f"{frame.filename} {frame.lineno}"), e)
            return ('created', 'updated')


@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'get_nr_workouts', 'get_workouts')


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'get_nr_workouts', 'get_workouts')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    search_fields = ['name', 'source__name', 'types__name']
    autocomplete_fields = ['types', 'source']
    readonly_fields = ('created', 'updated', 'get_video')
    list_display_links = ('name',)
    list_display = ('get_workout_types', 'name', 'source', 'time_in_min',
                    'get_times_planned', 'get_times_done', 'headshot_video',
                    'stars', 'equipment')
    list_editable = ('stars', 'equipment')
    list_filter = [WorkoutTypeFilter, SourceFilter, 'stars']


@admin.register(DistanceActivity)
class DistanceActivity(admin.ModelAdmin):
    search_fields = ['date', 'distance']
    readonly_fields = ('created', 'updated')
    list_display = ('date', 'distance', 'duration')
    autocomplete_fields = ['date']


@admin.register(BodyMeasurement)
class BodyMeasurementAdmin(admin.ModelAdmin):
    search_fields = ['date']
    readonly_fields = ('created', 'updated')
    list_display = ('date', 'weight_kg', 'leg_left_cm', 'leg_right_cm',
                    'arm_left_cm', 'arm_right_cm', 'waist_cm', 'belly_in_cm',
                    'booty_in_cm', 'calc_bmi')
    list_editable = ('weight_kg', 'leg_left_cm', 'leg_right_cm',
                     'arm_left_cm', 'arm_right_cm', 'waist_cm', 'belly_in_cm',
                     'booty_in_cm')

    class Media:
        css = {
            'all': ('admin.css')
        }
