from rest_framework.viewsets import ModelViewSet

from ..models.retail import Retail
from ..serializers.retail import RetailSerializer, RetailCreateSerializer


class RetailViewSet(ModelViewSet):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return RetailSerializer

        if self.action == "create" or self.action == "partial_update":
            return RetailCreateSerializer

        return super().get_serializer_class()
