from rest_framework import serializers
from portal.models import Quotation


class QuotationCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
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
