from rest_framework import serializers

from ..models.distributor import Distributor
from .contact import ContactSerializer
from .product import ProductSerializer


class DistributorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distributor
        fields = "__all__"


class DistributorSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer()

    class Meta:
        model = Distributor
        fields = "__all__"
