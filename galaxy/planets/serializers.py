# STANDARD IMPORTS
from rest_framework import serializers

# PROJECT IMPORTS
from .models import ModelPlanets


class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPlanets
        fields = '__all__'
