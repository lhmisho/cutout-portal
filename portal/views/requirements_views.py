from rest_framework.response import Response
from rest_framework import generics, views, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from portal.models import Requirement
from portal.serializers.requirements_serializers import *
from portal.utils.custom_responses import prepare_success_response, prepare_error_response, prepare_generic_error


class RequirementsListAPiView(generics.ListAPIView):
    """
    API for Applicant Requirements List API
    """

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            requirements = Requirement.objects.filter(is_active=True)
            serializer = RequirementsModelSerializer(requirements, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                prepare_error_response(str(e)),
                status=status.HTTP_400_BAD_REQUEST
            )
