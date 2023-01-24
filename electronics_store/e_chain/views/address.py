from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from ..models.address import Address
from ..permissions import IsActiveUser
from ..serializers.address import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsActiveUser]
    pagination_class = LimitOffsetPagination
