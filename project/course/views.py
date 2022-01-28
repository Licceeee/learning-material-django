from django.views.generic import ListView, DetailView
from course.models import (Lesson, Course, Docs)


class CourseListView(ListView):
    template_name = 'course/course-list.html'
    model = Course


class CourseDetailView(DetailView):
    template_name = 'course/course-detail.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = "Course Overview"
        context['percentage'] = self.object.count_videos
        # SEO
        context['page_title'] = "Course Overview"
        context['page_description'] = "Overview of the course"
        return context
