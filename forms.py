from django import forms
from .models import Calorie,TOP

class CalorieForm(forms.ModelForm):
    class Meta:
     model=Calorie
     fields=['name','category','cal']


class TOPForm(forms.ModelForm):
    class Meta:
     model=TOP
     fields=['date','total_cal']