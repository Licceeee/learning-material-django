from django.urls import path
from .views import IndexView, WorkoutAutocomplete


urlpatterns = [
    path('<int:week_nr>/<int:week_year>/', IndexView.as_view(),
         name='workout'),
    path('autocomplete/workout/', WorkoutAutocomplete.as_view(),
         name='workout-autocomplete'),
]
