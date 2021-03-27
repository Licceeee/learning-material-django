from django.contrib import admin
from .models import (Topic, MaterialType, Material)


class MaterialsInline(admin.StackedInline):
    model = Material.topics.through
    extra = 1
    autocomplete_fields = ('material',)

class TopicInline(admin.StackedInline):
    model = Topic
    extra = 1


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = [MaterialsInline]
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
    autocomplete_fields = ['material_type', 'topics']
    list_display = ('title', 'get_topics', 'material_type', 'url', 'video',
                    'created', 'updated')
    list_filter = ('topics',)