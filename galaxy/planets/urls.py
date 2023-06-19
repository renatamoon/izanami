# STANDARD IMPORTS IMPORTS
from django.urls import path, include
from rest_framework import routers

# PROJECT IMPORTS
from . import views


routes = routers.DefaultRouter()

routes.register('get_data', views.LandingPageViewSetTreemap, basename='Landing Page')

urlpatterns = [
    path("", include(routes.urls)),
]
