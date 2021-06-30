from rest_framework import serializers
from portal.models import Order


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'job_title', 'total')


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'total',
            'addon',
            'job_title',
            'image_path',
            'image_type',
            'requirement',
            'save_metadata',
            'image_quantity',
            'need_clipping_path',
        ]
        read_only_fields = ['id', ]



