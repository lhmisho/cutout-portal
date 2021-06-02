from portal.models import Addons

from rest_framework import serializers


class AddonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addons
        fields = (
            '__all__'
        )
