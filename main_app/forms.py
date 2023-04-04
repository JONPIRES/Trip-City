from django.forms import ModelForm
from .models import Activities

class ActivitiesForm(ModelForm):
  class Meta:
    model = Activities
    fields = ['date', 'meal']