from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import (Category, Course, Teacher, Lesson, CourseDoc, LessonDoc)


# ================================================================== >> INLINES
class LessonInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Lesson
    extra = 1


class CourseDocInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = CourseDoc
    extra = 1


class LessonDocInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = LessonDoc
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin, CourseDocInlineAdmin]
    search_fields = ['title', 'teacher']
    list_display = ('title', 'teacher', 'folder_name', 'created', 'updated')
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
    inlines = [LessonDocInlineAdmin]
    search_fields = ['title']
    list_display = ('title', 'course', 'seen', 'created', 'updated')
    list_filter = ('course', 'seen')
    autocomplete_fields = ['course']
    readonly_fields = ('created', 'updated')


@admin.register(CourseDoc)
class CourseDocAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'course', 'created', 'updated')
    list_filter = ('course',)
    autocomplete_fields = ['course']
    readonly_fields = ('created', 'updated')


@admin.register(LessonDoc)
class LessonDocAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'lesson', 'created', 'updated')
    list_filter = ('lesson',)
    autocomplete_fields = ['lesson']
    readonly_fields = ('created', 'updated')