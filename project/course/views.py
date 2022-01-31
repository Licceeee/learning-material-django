from django.views.generic import ListView, DetailView, TemplateView
from course.models import (Category, Course, Lesson)


class CategoryListView(ListView):
    template_name = 'course/category-list.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CourseListView(TemplateView):
    template_name = 'course/course-list.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        def get_title():
            try:
                if self.kwargs['category_id']:
                    category = Category.objects.get(
                        id=self.kwargs['category_id'])
                    return category.name
            except Exception:
                return "All courses"
            return "All courses"

        def get_category_id_from_params():
            try:
                return self.kwargs['category_id']
            except Exception:
                return 0

        def get_courses():
            category_id = get_category_id_from_params()
            if category_id > 0:
                try:
                    return Course.objects.filter(category=category_id)
                except Exception as e:
                    print(f"  ----------- babafucker {e}")
                    return Course.objects.all()
            return Course.objects.all()

        context['title'] = get_title()
        context['courses'] = get_courses()
        return context


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
