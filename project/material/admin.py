from django.contrib import admin
from .models import (Topic, MaterialType, Material, Lecture, Exercise,
                     Category, SubCategory)


class MaterialsInline(admin.StackedInline):
    model = Material.topics.through
    extra = 1
    autocomplete_fields = ('material',)


class TopicInline(admin.StackedInline):
    model = Topic
    extra = 1


class LectureInline(admin.StackedInline):
    model = Lecture.topics.through
    extra = 1


class ExerciseInline(admin.StackedInline):
    model = Exercise.topics.through
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    list_filter = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']
    search_fields = ['name']
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    list_filter = ('name',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = [LectureInline, ExerciseInline, MaterialsInline]
    search_fields = ['name']
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    list_filter = ('name',)


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    list_filter = ('name',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['title', 'topic']
    readonly_fields = ('created', 'updated')
    autocomplete_fields = ['material_type', 'topics', 'subcategory']
    list_display = ('title', 'get_topics', 'material_type', 'url',
                    'created', 'updated')
    list_filter = ('topics',)


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    search_fields = ['title', 'topic']
    readonly_fields = ('created', 'updated')
    autocomplete_fields = ['topics']
    list_display = ('title', 'get_topics', 'video', 'date',
                    'created', 'updated')
    list_filter = ('topics', 'date')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    search_fields = ['title', 'topic']
    readonly_fields = ('created', 'updated')
    autocomplete_fields = ['topics', 'exercise_format', 'correction_format']
    list_display = ('title', 'get_topics', 'exercise_format', 'url_exercise',
                    'correction_format', 'url_correction', 'from_date',
                    'created', 'updated')
    list_filter = ('topics', 'from_date')
