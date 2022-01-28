from django.urls import path
from .views import TodaysRoutineView, WeekOverView, StatsView


urlpatterns = [
    path('todays-routine/<date>/', TodaysRoutineView.as_view(),
         name='todays-routine'),
    path('weekly-routines/<int:week_nr>/<int:week_year>/',
         WeekOverView.as_view(),
         name='weekly-routines'),
    path('stats/', StatsView.as_view(), name='stats'),
]
