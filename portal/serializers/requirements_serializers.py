from rest_framework import serializers
from portal.models import Requirement


class RequirementsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'title', 'options', 'is_active', 'is_default', 'is_product', 'is_portrait']


class RequirementsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'title', 'options', 'is_active', 'is_default', 'is_product', 'is_portrait']
        read_only_fields = ['id', ]
