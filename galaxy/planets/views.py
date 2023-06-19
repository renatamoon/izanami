# STANDARD IMPORTS
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class LandingPageViewSetTreemap(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        try:
            dynamic_filters = request.query_params
            # getUserRestriction(request, dynamic_filters)

            # data = LandingPageServices.get_treemap_directory_area_and_management_level(dynamic_filters)

            response = dict({
                    'status_code': status.HTTP_200_OK,
                    'message': 'OK',
                    'data': 0
            })
            return JsonResponse(response, safe=False)

        except Exception as e:
            response = dict({
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': e, })
            return JsonResponse(response, safe=False)
