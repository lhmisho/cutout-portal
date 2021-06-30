from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from portal.serializers.instruction_serializers import InstructionListSerializer
from portal.models import Instruction
from portal.utils.custom_responses import prepare_success_response, prepare_error_response


class InstructionListApiView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            requirements = Instruction.objects.filter()
            serializer = InstructionListSerializer(requirements, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                prepare_error_response(str(e)),
                status=status.HTTP_400_BAD_REQUEST
            )


