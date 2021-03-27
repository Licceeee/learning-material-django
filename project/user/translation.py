from modeltranslation.translator import register, TranslationOptions
from django.contrib.auth.models import Group
# from .models import (CustomUser)


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('name',)
