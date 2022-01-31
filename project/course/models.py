from django.db import models
from core.models import Timestamps


class Category(Timestamps):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    icon_source = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Teacher(Timestamps):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f"{self.name}"


class Course(Timestamps):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(Teacher, default=None, null=True,
                                on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100, unique=True, null=True)
    intro_video = models.CharField(max_length=500, blank=True, null=True)
    intro_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta(object):
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.title}"

    def count_videos(self):
        return self.lesson_set.count()


class Lesson(Timestamps):
    title = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, default=None, null=True,
                               on_delete=models.CASCADE)
    order = models.FloatField(null=True, blank=True)
    seen = models.BooleanField(default=False)
    sortable_inline_order = models.PositiveIntegerField(default=0, blank=False,
                                                        null=False)
    url = models.CharField(max_length=500, null=True, blank=True)

    class Meta(object):
        verbose_name = "Lesson"
        verbose_name_plural = "Lesson"
        ordering = ['sortable_inline_order']

    def __str__(self):
        return f"{self.title}"


class Docs(Timestamps):
    title = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, default=None, null=True,
                               on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    sortable_inline_order = models.PositiveIntegerField(default=0, blank=False,
                                                        null=False)
    file = models.FileField(default=None,
                            upload_to='uploads/',
                            null=True, blank=True)

    class Meta(object):
        verbose_name = "Docs"
        verbose_name_plural = "Docs"
        ordering = ['sortable_inline_order']

    def __str__(self):
        return f"{self.title}"
