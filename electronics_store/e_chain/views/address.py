from rest_framework.viewsets import ModelViewSet

from ..models.address import Address
from ..serializers.address import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
