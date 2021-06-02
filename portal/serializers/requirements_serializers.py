from rest_framework import serializers
from portal.models import Requirement


class RequirementsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['title', 'options', 'is_active', 'is_default']
