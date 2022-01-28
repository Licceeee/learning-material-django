from django.db import models
from datetime import datetime, timedelta
from core.models import Timestamps  # noqa
from django.utils.html import format_html
from core.libs.global_functions import get_video_format  # noqa


class WorkoutType(Timestamps):
    """Abs, Legs, Booty, Gods etc"""
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.name}"

    def get_workouts(self):
        tasks = " ".join([
            f'<a href="{workout.url}" target="_blank">{workout.name} - '
            f'{workout.time_in_min}\'</a><br>'
            for workout in self.workout_set.all()])
        return format_html(tasks)
    get_workouts.short_description = "Workouts"

    def get_nr_workouts(self):
        return self.workout_set.count()
    get_nr_workouts.short_description = "# Workouts"


class Source(Timestamps):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.name}"

    def get_workouts(self):
        tasks = " ".join([
            f'<a href="{workout.url}" target="_blank">{workout.name} - '
            f'{workout.time_in_min}\'</a><br>'
            for workout in self.workout_set.all()])
        return format_html(tasks)
    get_workouts.short_description = "Workouts"

    def get_nr_workouts(self):
        return self.workout_set.count()
    get_nr_workouts.short_description = "# Workouts"


class Workout(Timestamps):
    STARS = (
        (-1, -1),
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    types = models.ManyToManyField(WorkoutType)
    name = models.CharField(max_length=256, unique=True)
    source = models.ForeignKey(Source, null=True, on_delete=models.PROTECT)
    url = models.URLField(max_length=500, blank=True, null=True)
    time_in_min = models.FloatField(blank=False, null=True, verbose_name="Min")
    stars = models.IntegerField(default=0, choices=STARS)
    equipment = models.BooleanField(default=False)

    def __str__(self):
        types = ", ".join([type.name for type in self.types.all()])
        return f"{self.name} ({self.time_in_min}) [{types}]"

    def get_types(self):
        return ", ".join([type.name for type in self.types.all()])

    def get_workout_types(self):
        return ", ".join([type.name for type in self.types.all()])

    get_workout_types.short_description = "Types"

    def get_times_planned(self):
        return len(self.workoutplan_set.filter(done=True))
    get_times_planned.short_description = "# planned"

    def get_times_done(self):
        return len(self.workoutplan_set.all())
    get_times_done.short_description = "# done"

    def headshot_video(self):
        return get_video_format(self.url, 200, 100)
    headshot_video.short_description = 'Preview'

    def get_video(self):
        return get_video_format(self.url, 500, 300)
    get_video.short_description = 'Preview'


class Exercise(Timestamps):
    name = models.CharField(max_length=256, unique=True)
    areas = models.ManyToManyField(WorkoutType)

    def __str__(self):
        return self.name


class WorkoutPlan(Timestamps):
    workout = models.ForeignKey(Workout, default=None,
                                on_delete=models.PROTECT)
    date = models.ForeignKey('routine.WorkoutDailyRoutine', null=True,
                             on_delete=models.PROTECT)
    time_needed_in_min = models.FloatField(blank=True, null=True)
    done = models.BooleanField(default=False)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return (f"{self.workout.name}")

    def get_workout_time(self):
        return self.workout.time_in_min
    get_workout_time.short_description = "Min"

    def get_workout_done_time(self):
        if self.done:
            if self.time_needed_in_min:
                return self.time_needed_in_min
            return self.workout.time_in_min
    get_workout_done_time.short_description = "Min done"


class DistanceActivity(Timestamps):
    ACTIVITY = (
        ("W", "Walk"),
        ("R", "Run")
    )

    date = models.ForeignKey('routine.WorkoutDailyRoutine', default=None,
                             on_delete=models.PROTECT)
    activity = models.CharField(max_length=2, choices=ACTIVITY, default="W")
    distance = models.FloatField()
    duration = models.DurationField(default=timedelta(minutes=120))

    def __str__(self):
        return f"{self.date} {self.activity} {self.distance}"


class BodyMeasurement(Timestamps):
    date = models.DateField(default=datetime.now, unique=True)

    weight_kg = models.FloatField(null=True, blank=True)
    leg_left_cm = models.FloatField(null=True, blank=True)
    leg_right_cm = models.FloatField(null=True, blank=True)
    arm_left_cm = models.FloatField(null=True, blank=True)
    arm_right_cm = models.FloatField(null=True, blank=True)
    waist_cm = models.FloatField(null=True, blank=True)
    belly_in_cm = models.FloatField(null=True, blank=True)
    booty_in_cm = models.FloatField(null=True, blank=True)

    def __str__(self):
        return (f"{self.date} {self.weight_kg}")

    def calc_bmi(self):
        try:
            return round(self.weight_kg / 156 / 156 * 10000, 2)
        except Exception:
            return "/"
    calc_bmi.short_description = "BMI"