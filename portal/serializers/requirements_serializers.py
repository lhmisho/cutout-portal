from rest_framework import serializers
from portal.models import Requirement
from rest_framework import status


class RequirementsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'title', 'options', 'is_active', 'is_default']


class RequirementsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'title', 'options', 'is_active', 'is_default']
