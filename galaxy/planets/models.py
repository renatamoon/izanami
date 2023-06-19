# STANDARD IMPORTS
from django.db import models


class ModelPlanets(models.Model):
    planet_name = models.CharField(max_length=100)
    chemical_elements = models.CharField(max_length=999)
    water_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    distance = models.FloatField()  # distance from alpha R
    LIFE_PROBABILITY = (
        ("UC", "uncertain"),
        ("L", "likely"),
        ("UL", "unlikely"),
    )
    probability = models.CharField(max_length=255, choices=LIFE_PROBABILITY)
