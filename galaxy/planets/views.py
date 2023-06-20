# THIRD PARTY IMPORTS
from django.http import JsonResponse
from rest_framework import viewsets, status
from django.shortcuts import render, redirect

# PROJECT IMPORTS
from .forms import PlanetForm
from .models import ModelPlanets


class ListPlanetViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            planets = ModelPlanets.objects.all()
            return render(request, "planet_list.html", {'planets': planets})

        except Exception as e:
            response = {
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': e
            }
            return JsonResponse(response, safe=False)


class CreatePlanetViewSet(viewsets.ViewSet):
    def post(self, request):
        try:
            if request.method == "POST":
                form = PlanetForm(request.POST)

                if form.is_valid():
                    form.save()
                    model = form.instance
                    return redirect('planet_list')

            else:
                form = PlanetForm()
            return render(request, 'planet_create.html', {'form': form})

        except Exception as e:
            response = {
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': e
            }
            return JsonResponse(response, safe=False)


class UpdatePlanetViewSet(viewsets.ViewSet):
    def put(self, request, id):
        try:
            planet = ModelPlanets.objects.get(id=id)
            form = PlanetForm(
                initial={
                    'planet_name': planet.planet_name,
                    'chemical_elements': planet.chemical_elements,
                    'water_percentage': planet.water_percentage,
                    'distance': planet.distance,
                    'probability': planet.probability
                }
            )

            if request.method == "POST":
                form = PlanetForm(request.POST, instance=planet)

                if form.is_valid():
                    form.save()
                    model = form.instance
                    return redirect('/planet_list')

            return render(request, 'planet_update.html', {'form': form})

        except Exception as e:
            response = {
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': e
            }
            return JsonResponse(response, safe=False)


class DeletePlanetViewSet(viewsets.ViewSet):
    def delete(self, request, id):
        try:
            planet = ModelPlanets.objects.get(id=id)
            planet.delete()

            return redirect('planet_list')

        except Exception as e:
            response = {
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': e
            }
            return JsonResponse(response, safe=False)
