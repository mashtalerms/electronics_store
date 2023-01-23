from rest_framework.viewsets import ModelViewSet

from ..models.factory import Factory
from ..serializers.factory import FactorySerializer, FactoryCreateSerializer


class FactoryViewSet(ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return FactorySerializer

        if self.action == "create" or self.action == "partial_update":
            return FactoryCreateSerializer

        return super().get_serializer_class()
