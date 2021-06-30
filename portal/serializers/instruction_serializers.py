from rest_framework import serializers
from portal.models import Instruction


class InstructionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['job_title', 'requirement', 'addon']
