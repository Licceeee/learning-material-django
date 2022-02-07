from django.db import models
from core.models import Timestamps
from core.libs.core_libs import (get_headshot_image, get_image_format)  # noqa
from uuid import uuid4


def img_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        # set filename as random string
        filename = f'{uuid4().hex}.{ext}'
    return (f'courses/intro_images/{filename}')


class Category(Timestamps):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    icon_source = models.CharField(max_length=500, null=True, blank=True)
    online = models.BooleanField(default=False)

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
    category = models.ForeignKey(Category, default=None, null=True,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(Teacher, default=None, null=True,
                                on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100, unique=True, null=True)
    image = models.ImageField(upload_to=img_upload_path, null=True,
                              blank=True)

    class Meta(object):
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.title}"

    def count_videos(self):
        return self.lesson_set.count()
    count_videos.short_description = '# Videos'

    def headshot_image(self):
        return get_headshot_image(self.image, 300)
    headshot_image.short_description = 'Preview'

    def get_image(self):
        if self.image:
            return get_image_format(self.image, 100)
        else:
            return "No Image"
    get_image.short_description = 'Image'


class Lesson(Timestamps):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, default=None, null=True,
                               on_delete=models.CASCADE)
    day = models.IntegerField(null=True, blank=True)
    sortable_inline_order = models.PositiveIntegerField(default=0, blank=False,
                                                        null=False)
    url = models.CharField(max_length=500, null=True, blank=True)

    class Meta(object):
        verbose_name = "Lesson"
        verbose_name_plural = "Lesson"
        ordering = ['sortable_inline_order']

    def __str__(self):
        return f"{self.title}"


class CourseDoc(Timestamps):
    title = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, default=None, null=True,
                               on_delete=models.CASCADE)
    sortable_inline_order = models.PositiveIntegerField(default=0, blank=False,
                                                        null=False)
    day = models.IntegerField(null=True, blank=True)
    file = models.FileField(default=None,
                            upload_to='uploads/',
                            null=True, blank=True)

    class Meta(object):
        verbose_name = "Course Doc"
        verbose_name_plural = "Course Docs"
        ordering = ['sortable_inline_order']

    def __str__(self):
        return f"{self.title}"
