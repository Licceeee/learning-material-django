from django.urls import path
from .views import TopicListView, TopicDetailView


urlpatterns = [
    path('', TopicListView.as_view(), name='topics'),
    path('<int:pk>', TopicDetailView.as_view(), name='topic-detail'),
]
