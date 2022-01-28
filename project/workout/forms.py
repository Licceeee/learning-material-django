from dal import autocomplete  # noqa
from django import forms
from .models import WorkoutPlan, Workout


class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ('__all__')
        widgets = {
            'workout': autocomplete.ModelSelect2(url='workout-autocomplete')
        }
