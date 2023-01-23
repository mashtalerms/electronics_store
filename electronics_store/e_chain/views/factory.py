from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..filters.factory import FactoryFilter
from ..models.factory import Factory
from ..permissions import IsActiveUser
from ..serializers.factory import FactorySerializer, FactoryCreateSerializer, FactoryUpdateSerializer
from rest_framework.decorators import action
from django.db.models import Avg


class FactoryViewSet(ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contacts__address_country', 'products__id')
    filterset_class = FactoryFilter
    permission_classes = [IsActiveUser]
    pagination_class = LimitOffsetPagination


    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return FactorySerializer

        if self.action == "create":
            return FactoryCreateSerializer

        if self.action == "partial_update":
            return FactoryUpdateSerializer

        return super().get_serializer_class()

    @action(
        detail=False, methods=['GET'], url_path=r'avg_debt', name='Get objects that has debt greater than all objects ')
    def get_objects_with_gt_debt(self, request, *args, **kwargs):
        avg_debt = Factory.objects.aggregate(Avg('debt'))
        objects = Factory.objects.annotate(Avg('debt'))
        result = [x for x in objects if x.debt > avg_debt['debt__avg']]
        return Response(FactorySerializer(result, many=True).data)
