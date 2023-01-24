from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from ..filters.distributor import DistributorFilter
from ..models.distributor import Distributor
from ..permissions import IsActiveUser
from ..serializers.distributor import DistributorSerializer, DistributorCreateSerializer, DistributorUpdateSerializer
from rest_framework.decorators import action
from django.db.models import Avg


class DistributorViewSet(ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contacts__address_country', 'products__id')
    filterset_class = DistributorFilter
    permission_classes = [IsActiveUser]
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return DistributorSerializer

        if self.action == "create":
            return DistributorCreateSerializer

        if self.action == "partial_update":
            return DistributorUpdateSerializer

        return super().get_serializer_class()

    @action(
        detail=False, methods=['GET'], url_path=r'avg_debt', name='Get objects that has debt greater than all objects ')
    def get_objects_with_gt_debt(self, request, *args, **kwargs):
        avg_debt = Distributor.objects.aggregate(Avg('debt'))
        objects = Distributor.objects.annotate(Avg('debt'))
        result = [x for x in objects if x.debt > avg_debt['debt__avg']]
        return Response(DistributorSerializer(result, many=True).data)
