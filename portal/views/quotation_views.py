from rest_framework.response import Response
from rest_framework import generics, views, status

from portal.serializers.quotation_serializers import QuotationCreateUpdateSerializer
from portal.utils.custom_responses import prepare_create_success_response, prepare_error_response
from portal.services.validation_service import validate_quotation_data


def prepare_quotation_data(quotation_data):
    data = {}
    data.update({'addon': quotation_data.get('addon')})
    data.update({'job_title': quotation_data.get('job_title')})
    data.update({'image_type': quotation_data.get('image_type')})
    data.update({'requirement': quotation_data.get('requirement')})
    data.update({'save_metadata': quotation_data.get('save_metadata')})
    data.update({'image_quantity': quotation_data.get('image_quantity')})
    data.update({'need_clipping_path': quotation_data.get('need_clipping_path')})
    data.update({'image_path': quotation_data.get('image') if quotation_data.get('image',
                                                                                 None) is not None else quotation_data.get(
        'image_path', None)})
    return data


class QuotationCreateView(views.APIView):
    def post(self, request, format=None):
        validate_error = validate_quotation_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        data = prepare_quotation_data(request.data)
        serializer = QuotationCreateUpdateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
