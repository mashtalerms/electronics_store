from django_filters import rest_framework as filters

from ..models.dealership import Dealership


class DealershipFilter(filters.FilterSet):
    country = filters.CharFilter(field_name="contacts__address__country", lookup_expr='iexact')
    product = filters.NumberFilter(field_name="products__id", lookup_expr='exact')

    class Meta:
        model = Dealership
        fields = ["contacts", "product"]
