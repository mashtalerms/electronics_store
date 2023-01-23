from django_filters import rest_framework as filters

from ..models.retail import Retail


class RetailFilter(filters.FilterSet):
    country = filters.CharFilter(field_name="contacts__address__country", lookup_expr='iexact')
    product = filters.NumberFilter(field_name="products__id", lookup_expr='exact')

    class Meta:
        model = Retail
        fields = ["contacts", "product"]
