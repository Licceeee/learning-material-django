from django.views.generic import ListView, DetailView, TemplateView
from course.models import (Category, Course, Lesson)


class CategoryListView(ListView):
    template_name = 'course/category-list.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Category.objects.filter(online=True)
        return context


class CourseListView(TemplateView):
    template_name = 'course/course-list.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        def get_category_id_from_params():
            try:
                return self.kwargs['category_id']
            except Exception:
                return None

        def get_category_infos():
            """Return title, description, courses of category"""
            category_id = get_category_id_from_params()
            if category_id:
                try:
                    category = Category.objects.get(
                        id=category_id)
                    return (category.name, category.description,
                            Course.objects.filter(category=category_id))
                except Exception:
                    pass
            return ("All courses", "Browse through all the courses",
                    Course.objects.all())

        context['title'] = get_category_infos()[0]
        context['description'] = get_category_infos()[1]
        context['courses'] = get_category_infos()[2]
        return context


class CourseDetailView(DetailView):
    template_name = 'course/course-detail.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = "Course Overview"
        context['nr_lessons'] = self.object.count_videos
        # SEO
        context['page_title'] = "Course Overview"
        context['page_description'] = "Overview of the course"
        return context
