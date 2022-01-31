from django.urls import path
from .views import (CourseListView, CourseDetailView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(CourseListView.as_view()), name='course-list'),
    path('<int:pk>', CourseDetailView.as_view(),
         name='course-detail'),
]
