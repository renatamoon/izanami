# THIRD PARTY IMPORTS
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView

# PROJECT IMPORTS
from galaxy.planets.models import ModelPlanets
from galaxy.planets.serializers import PlanetsSerializer


class PlanetCreateListViewSet(APIView):
    queryset = ModelPlanets.objects.all()
    serializer_class = PlanetsSerializer

    def get_planets(self, request, *args, **kwargs):
        """List all the planets items"""

        planets = ModelPlanets.objects
        serializer = PlanetsSerializer(planets, many=True)

        response = {
            'status_code': status.HTTP_200_OK,
            'message': 'OK',
            'data': serializer.data
        }
        return JsonResponse(response, safe=False)

    def post(self, request, *args, **kwargs):
        """Create data for planets with given params"""

        data = {
            'planet_name': request.data.get('planet_name'),
            'chemical_elements': request.data.get('chemical_elements'),
            'water_percentage': request.data.get('water_percentage'),
            'distance': request.data.get('distance'),
            'probability': request.data.get('probability')
        }

        serializer = PlanetsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': 'OK',
                'data': serializer.data
            }
            return JsonResponse(response, safe=False)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
