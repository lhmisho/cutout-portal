from rest_framework import serializers
from portal.models import Instruction


class InstructionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['id', 'job_title']
        read_only_fields = ['id', ]

class InstructionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['id', 'job_title', 'requirement', 'addon']
        read_only_fields = ['id', ]

