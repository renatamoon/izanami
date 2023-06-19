# STANDARD IMPORTS
from rest_framework import viewsets, status
from django.http import JsonResponse

from galaxy.planets.services import PlanetServices


class PlanetRegistrationViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            params = request.query_params
            response = PlanetServices.get_planets(params)

            response = dict({
                    'status_code': status.HTTP_200_OK,
                    'message': 'OK',
                    'data': response
            })
            return JsonResponse(response, safe=False)

        except Exception as e:
            response = dict({
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': e, })
            return JsonResponse(response, safe=False)
