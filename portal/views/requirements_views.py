import json

from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics, views, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from portal.models import Requirement
from portal.serializers.requirements_serializers import *
from portal.utils.custom_responses import (prepare_success_response, prepare_error_response,
                                           prepare_generic_error, prepare_create_success_response)
from portal.services.validation_service import *

class RequirementsListAPiView(generics.ListAPIView):
    """
    API for Applicant Requirements List API
    """

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            requirements = Requirement.objects.filter(is_active=True)
            serializer = RequirementsModelSerializer(requirements, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                prepare_error_response(str(e)),
                status=status.HTTP_400_BAD_REQUEST
            )


class RequirementsCreateApiView(views.APIView):

    def get_object(self, pk):
        try:
            return Requirement.objects.filter(id=pk).first()
        except Requirement.DoesNotExist:
            return None
    ''
    def post(self, request, format=None):
        validate_error = validate_requirements_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = RequirementsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        validate_error = validate_requirements_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        requirement = Requirement.objects.filter(id=pk).first()
        if requirement is not None:
            serializer = RequirementsCreateSerializer(requirement, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(prepare_error_response("No data found for this ID"), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        requirement = self.get_object(pk)
        if requirement is not None:
            requirement.delete()
            return Response(prepare_success_response("Data deleted successfully"), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)