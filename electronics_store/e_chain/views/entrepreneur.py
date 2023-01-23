from rest_framework.viewsets import ModelViewSet

from ..models.entrepreneur import Entrepreneur
from ..serializers.entrepreneur import EntrepreneurSerializer, EntrepreneurCreateSerializer


class EntrepreneurViewSet(ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return EntrepreneurSerializer

        if self.action == "create" or self.action == "partial_update":
            return EntrepreneurCreateSerializer

        return super().get_serializer_class()
