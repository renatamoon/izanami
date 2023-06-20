# THIRD PARTY IMPORTS
from django import forms

# PROJECT IMPORTS
from .models import *


class PlanetForm(forms.ModelForm):
    class Meta:
        model = ModelPlanets
        fields = '__all__'
