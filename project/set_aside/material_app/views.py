from django.views.generic import ListView, DetailView
from django.utils.translation import ugettext_lazy as _
from .models import (Topic, Category, SubCategory, Material)


class CategoryListView(ListView):
    template_name = 'material/categories.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Categories Overview")
        # SEO
        context['page_title'] = _("Categories Overview")
        context['page_description'] = _("Overview of all Categories")
        return context


class CategoryDetailView(DetailView):
    template_name = 'material/category.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Category")
        # SEO
        context['page_title'] = _("Category")
        context['page_description'] = _("Category")
        return context


class SubCategoryDetailView(DetailView):
    template_name = 'material/subcategory.html'
    model = SubCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("SubCategory")
        # SEO
        context['page_title'] = _("SubCategory")
        context['page_description'] = _("SubCategory")
        return context


class MaterialDetailView(DetailView):
    template_name = 'material/material.html'
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Material")
        # SEO
        context['page_title'] = _("Material")
        context['page_description'] = _("Material")
        return context


class TopicListView(ListView):
    template_name = 'material/topics.html'
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Topic Overview")
        # SEO
        context['page_title'] = _("Topic Overview")
        context['page_description'] = _("Overview of all topics")
        return context


class TopicDetailView(DetailView):
    template_name = 'material/topic.html'
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Topic")
        # SEO
        context['page_title'] = _("Topic")
        context['page_description'] = _("Topic")
        return context
