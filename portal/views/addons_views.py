from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from portal.models import Addons
from portal.serializers.addons_serializers import AddonsSerializer


class AddonsViewSet(viewsets.ModelViewSet):
    queryset = Addons.objects.all()
    serializer_class = AddonsSerializer
    permission_classes = [IsAdminUser, ]
