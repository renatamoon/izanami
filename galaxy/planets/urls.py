# THIRD PARTY IMPORTS
from django.urls import path, include
from rest_framework import routers

# PROJECT IMPORTS
from . import views


routes = routers.DefaultRouter()

routes.register('planets_api', views.PlanetCreateListViewSet, basename='Create List Planets')

urlpatterns = [
    path("", include(routes.urls)),
]
