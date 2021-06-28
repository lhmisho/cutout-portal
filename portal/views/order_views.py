from rest_framework.response import Response
from rest_framework import generics, views, status

from portal.serializers.order_serializers import OrderCreateUpdateSerializer
from portal.utils.custom_responses import prepare_create_success_response, prepare_error_response
from portal.services.validation_service import validate_order_data


def prepare_order_data(order_data):
    data = {}
    data.update({'job_title': order_data.get('job_title')})
    data.update({'image_path': order_data.get('image') if order_data.get('image', None) is not None else order_data.get('image_path', None)})
    data.update({'image_type': order_data.get('image_type')})
    data.update({'requirement': order_data.get('requirement')})
    data.update({'addon': order_data.get('addon')})
    data.update({'save_metadata': order_data.get('save_metadata')})
    data.update({'image_quantity': order_data.get('image_quantity')})
    data.update({'need_clipping_path': order_data.get('need_clipping_path')})
    return data


class OrderCreateView(views.APIView):
    def post(self, request, format=None):
        validate_error = validate_order_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        data = prepare_order_data(request.data)
        serializer = OrderCreateUpdateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
