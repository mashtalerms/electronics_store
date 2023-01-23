from rest_framework.viewsets import ModelViewSet

from ..models.distributor import Distributor
from ..serializers.distributor import DistributorSerializer, DistributorCreateSerializer


class DistributorViewSet(ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return DistributorSerializer

        if self.action == "create" or self.action == "partial_update":
            return DistributorCreateSerializer

        return super().get_serializer_class()
