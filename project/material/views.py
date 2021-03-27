from django.views.generic import ListView, DetailView
from .models import Topic
from django.utils.translation import ugettext_lazy as _


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