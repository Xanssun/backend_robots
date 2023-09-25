from .models import Robot
from django import forms


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = '__all__'
