from django.urls import path
from .views import (TopicListView, TopicDetailView, CategoryListView,
                    CategoryDetailView, SubCategoryDetailView,
                    MaterialDetailView)


urlpatterns = [
    path('', TopicListView.as_view(), name='topics'),
    path('<int:pk>', TopicDetailView.as_view(), name='topic-detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryDetailView.as_view(),
         name='category-detail'),
    path('subcategory/<int:pk>', SubCategoryDetailView.as_view(),
         name='subcategory-detail'),
    path('material/<int:pk>', MaterialDetailView.as_view(),
         name='material-detail'),
]
