from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import (Category, Course, Teacher, Lesson, CourseDoc,
                     CourseUser, LessonUser)


# ================================================================== >> INLINES
class LessonInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Lesson
    extra = 1


class CourseDocInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = CourseDoc
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin, CourseDocInlineAdmin]
    search_fields = ['title', 'teacher']
    list_display = ('title', 'teacher', 'category', 'count_videos',
                    'get_image')
    list_filter = ('title', 'teacher')
    autocomplete_fields = ['teacher', 'category']
    readonly_fields = ('created', 'updated', 'headshot_image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'description', 'online', 'count_courses', 
                    'created', 'updated')
    list_editable = ('online',)
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
    list_display = ('title', 'course', 'day', 'created', 'updated')
    list_filter = ('course',)
    autocomplete_fields = ['course']
    readonly_fields = ('created', 'updated')


@admin.register(CourseDoc)
class CourseDocAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'course', 'created', 'updated')
    list_filter = ('course',)
    autocomplete_fields = ['course']
    readonly_fields = ('created', 'updated')


@admin.register(CourseUser)
class CourseUserAdmin(admin.ModelAdmin):
    search_fields = ['user', 'course']
    list_display = ('user', 'course', 'completed', 'created', 'updated')
    list_filter = ('completed',)
    autocomplete_fields = ['user', 'course']
    readonly_fields = ('created', 'updated')


@admin.register(LessonUser)
class LessonUserAdmin(admin.ModelAdmin):
    search_fields = ['user', 'lesson']
    list_display = ('user', 'lesson', 'completed', 'created', 'updated')
    list_filter = ('completed',)
    autocomplete_fields = ['user', 'lesson']
    readonly_fields = ('created', 'updated')
