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


# # ================================================================= >> OLD CRAP


# class WorkoutRoutine(Timestamps):
#     date = models.DateField(default=datetime.now, unique=True)
#     # TODO add unique together user and date

#     class Meta:
#         ordering = ['-date']

#     def __str__(self):
#         return f"{self.date.strftime('%d %B %Y')} - {self.date.strftime('%A')}"

#     def get_nr_tasks(self):
#         res = self.plan_set.count()
#         if res > 0:
#             return res
#     get_nr_tasks.short_description = "# Total Tasks"

#     def get_nr_todo_tasks(self):
#         res = self.plan_set.filter(done=False).count()
#         if res > 0:
#             return res
#     get_nr_todo_tasks.short_description = "# Tasks ToDo"

#     def get_nr_done_tasks(self):
#         res = self.plan_set.filter(done=True).count()
#         if res > 0:
#             return res
#     get_nr_done_tasks.short_description = "# Tasks Done"

#     def get_tasks_tot_time(self):
#         time = 0
#         for plan in self.plan_set.all():
#             if plan.task.time_in_min:
#                 time += plan.task.time_in_min
#         if time > 0:
#             return f"{time} min"
#     get_tasks_tot_time.short_description = "Total Time"

#     def get_tasks_done_time(self):
#         time = 0
#         for plan in self.plan_set.filter(done=True):
#             if plan.task.time_in_min:
#                 time += plan.task.time_in_min
#         if time > 0:
#             return format_html(f'<b style="color: green;">{time} min</b>')
#     get_tasks_done_time.short_description = "Time Done Tasks"

#     def get_subcats(self):
#         """Get subcategories"""
#         subcats = ""
#         for plan in self.plan_set.all():
#             print("arrives")
#             print(plan.task.sub_categories)
#             for sub in plan.task.sub_categories.all():
#                 if sub.name not in subcats:
#                     subcats += (f'{sub.name}<br>')
#         return format_html(subcats)
#     get_subcats.short_description = "SubCats"

#     def get_weekday(self):
#         return _get_weekday(self.date)
#     get_weekday.short_description = "Day"


# class Source(Timestamps):
#     name = models.CharField(max_length=256, unique=True)

#     def __str__(self):
#         return f"{self.name}"


# class Category(Timestamps):
#     """Workout, Study, Drawing"""
#     name = models.CharField(max_length=256, unique=True)
#     # add user and unique together user and name
#     display_in_stats = models.BooleanField(
#         default=True, verbose_name="Display in week overview")

#     def __str__(self):
#         return f"{self.name}"

#     def get_icon(self):
#         # style:fas,icon:allergies
#         icon = []
#         placeholder = ""
#         if self.icon:
#             string = str(self.icon)
#             for word in string.split(','):
#                 if 'style:' in word:
#                     word = word.replace('style:', '')
#                     icon.append(word)
#                 if 'icon:' in word:
#                     word = word.replace('icon:', '')
#                     icon.append(word)
#             return format_html(f'<i class="{icon[0]} fa-{icon[1]} fa-stack-1x '
#                                f'icon-color"></i>')
#     get_icon.short_description = "Icon"


# class SubCategory(Timestamps):
#     """Abs, Legs, Booty, Gods etc"""
#     name = models.CharField(max_length=256)
#     category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)

#     class Meta:
#         unique_together = ['name', 'category']

#     def __str__(self):
#         return f"{self.name}"

#     def get_tasks(self):
#         tasks = " ".join([
#             f'<a href="{task.url}" target="_blank">{task.name} - '
#             f'{task.time_in_min}\'</a><br>'
#             for task in self.task_set.all()])
#         return format_html(tasks)
#     get_tasks.short_description = "Tasks"

#     def get_nr_tasks(self):
#         return self.task_set.count()
#     get_nr_tasks.short_description = "# Tasks"


# class Task(Timestamps):
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)
#     sub_categories = models.ManyToManyField(SubCategory)
#     name = models.CharField(max_length=256, unique=True)
#     source = models.ForeignKey(Source, null=True, blank=True,
#                                on_delete=models.PROTECT)
#     url = models.URLField(max_length=500, blank=True, null=True)
#     time_in_min = models.PositiveIntegerField(blank=False, null=True,
#                                               verbose_name="Min")

#     class Meta:
#         unique_together = ['name', 'time_in_min']

#     def __str__(self):
#         types = ", ".join([type.name for type in self.sub_categories.all()])
#         return f"{types}: {self.name} - {self.time_in_min}'"

#     def get_sub_categories(self):
#         return ", ".join([sub.name for sub in self.sub_categories.all()])
#     get_sub_categories.short_description = "Sub Categories"

#     def get_times_planned(self):
#         nr = self.plan_set.count()
#         if nr > 0:
#             return nr
#     get_times_planned.short_description = "# planned"

#     def get_times_done(self):
#         nr = self.plan_set.filter(done=True).count()
#         if nr > 0:
#             return nr
#     get_times_done.short_description = "# done"


# class Plan(Timestamps):
#     task = models.ForeignKey(Task, default=None, on_delete=models.PROTECT)
#     day = models.ForeignKey(WorkoutRoutine, default=None,
#                             on_delete=models.DO_NOTHING)
#     time = models.TimeField(auto_now_add=False)
#     done = models.BooleanField(default=False)

#     class Meta:
#         unique_together = ['day', 'time']
#         ordering = ['day', 'time']

#     def __str__(self):
#         return (f"{self.task.category.name} - {self.task.name}")

#     def get_weekday(self):
#         return _get_weekday(self.day.date)
#     get_weekday.short_description = "Day"
