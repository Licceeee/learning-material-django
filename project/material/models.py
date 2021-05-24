from django.db import models
from core.models import Timestamps
from uuid import uuid4
from datetime import datetime


def upload_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        # set filename as random string
        filename = f'{uuid4().hex}.{ext}'
    return (f'uploads/{filename}')


def upload_video_path(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        # set filename as random string
        filename = f'{uuid4().hex}.{ext}'
    return (f'uploads/videos/{filename}')



class Topic(Timestamps):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return f"{self.name}"


class MaterialType(Timestamps):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Material type"
        verbose_name_plural = "Material types"

    def __str__(self):
        return f"{self.name}"


class Category(Timestamps):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class SubCategory(Timestamps):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, default=None, null=True,
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return f"{self.name}"


class Material(Timestamps):
    title = models.CharField(max_length=100)
    topics = models.ManyToManyField(Topic)
    subcategory = models.ForeignKey(SubCategory, default=None, null=True,
                                    on_delete=models.CASCADE)
    material_type = models.ForeignKey(MaterialType, default=None,
                                      on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)
    video = models.FileField(default=None, upload_to=upload_video_path,
                             null=True, blank=True)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def __str__(self):
        return f"{self.title}"

    def get_topics(self):
        return ", ".join([
            topic.name for topic in self.topics.all()])
    get_topics.short_description = "Topics"


class Lecture(Timestamps):
    title = models.CharField(max_length=100)
    topics = models.ManyToManyField(Topic)
    video = models.FileField(default=None, upload_to=upload_dir_path,
                             null=True, blank=True)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.title}"

    def get_topics(self):
        return ", ".join([
            topic.name for topic in self.topics.all()])
    get_topics.short_description = "Topics"


class Exercise(Timestamps):
    title = models.CharField(max_length=100)
    topics = models.ManyToManyField(Topic)
    exercise_format = models.ForeignKey(MaterialType, default=None,
                                        related_name="exercise",
                                        on_delete=models.CASCADE)
    url_exercise = models.URLField(null=True, blank=True)
    correction_format = models.ForeignKey(MaterialType, default=None,
                                          related_name="correction",
                                          on_delete=models.CASCADE)
    url_correction = models.URLField(null=True, blank=True)
    from_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.title}"

    def get_topics(self):
        return ", ".join([
            topic.name for topic in self.topics.all()])
    get_topics.short_description = "Topics"
