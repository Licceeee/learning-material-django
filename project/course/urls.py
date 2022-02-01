from django.urls import path
from .views import (CategoryListView, CourseListView, CourseDetailView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(CategoryListView.as_view()), name='category-list'),
    path('<int:category_id>/courses', login_required(CourseListView.as_view()),
         name='course-list'),
    path('courses/', login_required(CourseListView.as_view()),
         name='course-list'),
    path('courses/<int:pk>', CourseDetailView.as_view(),
         name='course-detail'),
]
