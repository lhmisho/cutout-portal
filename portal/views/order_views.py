from rest_framework.response import Response
from rest_framework import generics, views, status

from portal.serializers.order_serializers import OrderCreateUpdateSerializer, OrderModelSerializer
from portal.utils.custom_responses import prepare_create_success_response, prepare_error_response, \
    prepare_success_response
from portal.services.validation_service import validate_order_data
from portal.models import Order
from portal.serializers.instruction_serializers import InstructionModelSerializer


def prepare_order_data(order_data):
    data = {}
    data.update({'addon': order_data.get('addon')})
    data.update({'job_title': order_data.get('job_title')})
    data.update({'image_type': order_data.get('image_type')})
    data.update({'requirement': order_data.get('requirement')})
    data.update({'save_metadata': order_data.get('save_metadata')})
    data.update({'image_quantity': order_data.get('image_quantity')})
    data.update({'need_clipping_path': order_data.get('need_clipping_path')})
    data.update({'image_path': order_data.get('image') if order_data.get('image', None) is not None else order_data.get('image_path', None)})

    # calculate price
    addons = order_data.get('addon')
    requirements = order_data.get('requirement')
    addons_price = sum([item.get('option_price') for item in addons])
    requirements_price = sum([item.get('option_price') for item in requirements])
    total = addons_price + requirements_price
    # update total to data
    data.update({'total': total})
    return data


def create_instruction(order_data):
    instruction = {}
    instruction.update({'job_title': order_data.get('job_title')})
    instruction.update({'requirement': order_data.get('requirement')})
    instruction.update({'addon': order_data.get('addon')})
    serializer = InstructionModelSerializer(data=instruction)
    if serializer.is_valid():
        serializer.save()


class OrderCreateView(views.APIView):
    def post(self, request, format=None):
        validate_error = validate_order_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        data = prepare_order_data(request.data)
        serializer = OrderCreateUpdateSerializer(data=data)

        # save instruction
        if request.data.get('save_instruction', False):
            try:
                create_instruction(request.data)
            except Exception as e:
                print(str(e))

        if serializer.is_valid():
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListAPiView(generics.ListAPIView):
    """
    API for Applicant Requirements List API
    """

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            requirements = Order.objects.filter()
            serializer = OrderModelSerializer(requirements, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                prepare_error_response(str(e)),
                status=status.HTTP_400_BAD_REQUEST
            )
