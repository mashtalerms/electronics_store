from rest_framework.viewsets import ModelViewSet

from ..models.dealership import Dealership
from ..serializers.dealership import DealershipSerializer, DealershipCreateSerializer


class DealershipViewSet(ModelViewSet):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return DealershipSerializer

        if self.action == "create" or self.action == "partial_update":
            return DealershipCreateSerializer

        return super().get_serializer_class()
