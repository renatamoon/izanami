# THIRD PARTY IMPORTS
from django.urls import path

# PROJECT IMPORTS
from . import views

urlpatterns = [
    path('planet_list', views.ListPlanetViewSet.as_view({'get': 'list'}), name='planet_list'),
    path('planet_create', views.CreatePlanetViewSet.as_view({'get': 'post'}), name='planet_create'),
    path('planet_update/<int:id>', views.UpdatePlanetViewSet.as_view({'get': 'put'}), name='planet_update'),
    path('planet_delete/<int:id>', views.DeletePlanetViewSet.as_view({'get': 'delete'}), name='planet_delete'),
]
