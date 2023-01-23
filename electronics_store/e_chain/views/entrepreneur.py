from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from ..filters.entrepreneur import EntrepreneurFilter
from ..models.entrepreneur import Entrepreneur
from ..permissions import IsActiveUser
from ..serializers.entrepreneur import EntrepreneurSerializer, EntrepreneurCreateSerializer, \
    EntrepreneurUpdateSerializer
from rest_framework.decorators import action
from django.db.models import Avg


class EntrepreneurViewSet(ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contacts__address_country', 'products__id')
    filterset_class = EntrepreneurFilter
    permission_classes = [IsActiveUser]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return EntrepreneurSerializer

        if self.action == "create":
            return EntrepreneurCreateSerializer

        if self.action == "partial_update":
            return EntrepreneurUpdateSerializer

        return super().get_serializer_class()

    @action(
        detail=False, methods=['GET'], url_path=r'avg_debt', name='Get objects that has debt greater than all objects ')
    def get_objects_with_gt_debt(self, request, *args, **kwargs):
        avg_debt = Entrepreneur.objects.aggregate(Avg('debt'))
        objects = Entrepreneur.objects.annotate(Avg('debt'))
        result = [x for x in objects if x.debt > avg_debt['debt__avg']]
        return Response(EntrepreneurSerializer(result, many=True).data)
