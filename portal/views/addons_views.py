from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics, views, status
from portal.utils.custom_responses import (prepare_success_response, prepare_error_response,
                                           prepare_generic_error, prepare_create_success_response)

from portal.services.validation_service import *
from portal.models import Addons
from portal.serializers.addons_serializers import AddonsSerializer


class AddonsListView(generics.ListAPIView):
    """
        API for Applicant Addons List API
    """
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request, *args, **kwargs):
        try:
            addons = Addons.objects.filter(is_active=True)
            serializer = AddonsSerializer(addons, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                prepare_error_response(str(e)),
                status=status.HTTP_400_BAD_REQUEST
            )


class AddonsCreateUpdateDeleteApiView(views.APIView):
    # permission_classes = [permissions.IsAdminUser, ]

    def get_object(self, pk):
        try:
            return Addons.objects.filter(id=pk).first()
        except Addons.DoesNotExist:
            return None

    def post(self, request, format=None):
        validate_error = validate_addons_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = AddonsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        validate_error = validate_requirements_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)

        addons = Addons.objects.filter(id=pk).first()
        if addons is not None:
            serializer = AddonsSerializer(addons, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(prepare_error_response("No addons found for this ID"), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        addons = self.get_object(pk)
        if addons is not None:
            addons.delete()
            return Response(prepare_success_response("Addons deleted successfully"), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)
