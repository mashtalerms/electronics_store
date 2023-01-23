from rest_framework import serializers

from ..models.dealership import Dealership
from .contact import ContactSerializer
from .product import ProductSerializer


class DealershipCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dealership
        fields = "__all__"


class DealershipSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer()

    class Meta:
        model = Dealership
        fields = "__all__"
