from django.views.generic import ListView, DetailView
from course.models import (Lesson, Course, Docs)


class CourseListView(ListView):
    template_name = 'course/course-list.html'
    model = Course


class CourseDetailView(DetailView):
    template_name = 'course/course-detail.html'
    model = Course
