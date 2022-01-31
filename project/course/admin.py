from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import (Category, Course, Teacher, Lesson, Docs)


# ================================================================== >> INLINES
class LessonInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Lesson
    extra = 1


class DocsInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Docs
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin, DocsInlineAdmin]
    search_fields = ['title', 'teacher']
    list_display = ('title', 'teacher', 'created', 'updated')
    list_filter = ('title', 'teacher')
    autocomplete_fields = ['teacher', 'category']
    readonly_fields = ('created', 'updated')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'description', 'created', 'updated')
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


@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'course', 'read', 'created', 'updated')
    list_filter = ('course', 'read')
    autocomplete_fields = ['course']
    readonly_fields = ('created', 'updated')
