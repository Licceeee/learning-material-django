from django.contrib import admin
from .models import (Course, Teacher, Lesson)
from adminsortable2.admin import SortableInlineAdminMixin


# ================================================================== >> INLINES
class LessonInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Lesson
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin]
    search_fields = ['title', 'teacher']
    list_display = ('title', 'teacher', 'created', 'updated')
    list_filter = ('title', 'teacher')
    autocomplete_fields = ['teacher']
    readonly_fields = ('created', 'updated')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'created', 'updated')
    list_filter = ('name',)
    readonly_fields = ('created', 'updated')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'course', 'seen', 'created', 'updated')
    list_filter = ('course', 'seen')
    autocomplete_fields = ['course']
    readonly_fields = ('created', 'updated')