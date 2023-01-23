from django_filters import rest_framework as filters

from ..models.entrepreneur import Entrepreneur


class EntrepreneurFilter(filters.FilterSet):
    country = filters.CharFilter(field_name="contacts__address__country", lookup_expr='iexact')
    product = filters.NumberFilter(field_name="products__id", lookup_expr='exact')

    class Meta:
        model = Entrepreneur
        fields = ["contacts", "product"]
