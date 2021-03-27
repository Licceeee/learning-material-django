from django.db import models
from core.models import Timestamps
from uuid import uuid4


def upload_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        # set filename as random string
        filename = f'{uuid4().hex}.{ext}'
    return (f'uploads/{filename}')


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


class Material(Timestamps):
    title = models.CharField(max_length=100)
    topics = models.ManyToManyField(Topic)
    material_type = models.ForeignKey(MaterialType, default=None,
                                      on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)
    video = models.FileField(default=None, upload_to=upload_dir_path,
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