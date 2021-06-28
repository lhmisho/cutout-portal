from rest_framework.response import Response
from rest_framework import generics, views, status

from portal.serializers.order_serializers import OrderCreateUpdateSerializer
from portal.utils.custom_responses import prepare_create_success_response, prepare_error_response
from portal.services.validation_service import validate_order_data


class OrderCreateView(views.APIView):
    def post(self, request, format=None):
        validate_error = validate_order_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = OrderCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
