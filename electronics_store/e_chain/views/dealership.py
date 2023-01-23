from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from ..filters.dealership import DealershipFilter
from ..models.dealership import Dealership
from ..permissions import IsActiveUser
from ..serializers.dealership import DealershipSerializer, DealershipCreateSerializer, DealershipUpdateSerializer
from rest_framework.decorators import action
from django.db.models import Avg


class DealershipViewSet(ModelViewSet):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contacts__address_country', 'products__id')
    filterset_class = DealershipFilter
    permission_classes = [IsActiveUser]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return DealershipSerializer

        if self.action == "create":
            return DealershipCreateSerializer

        if self.action == "partial_update":
            return DealershipUpdateSerializer

        return super().get_serializer_class()

    @action(
        detail=False, methods=['GET'], url_path=r'avg_debt', name='Get objects that has debt greater than all objects ')
    def get_objects_with_gt_debt(self, request, *args, **kwargs):
        avg_debt = Dealership.objects.aggregate(Avg('debt'))
        objects = Dealership.objects.annotate(Avg('debt'))
        result = [x for x in objects if x.debt > avg_debt['debt__avg']]
        return Response(DealershipSerializer(result, many=True).data)
