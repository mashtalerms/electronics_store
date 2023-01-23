from rest_framework import serializers

from ..models.retail import Retail
from .contact import ContactSerializer
from .product import ProductSerializer


class RetailCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Retail
        fields = "__all__"


class RetailSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer()

    class Meta:
        model = Retail
        fields = "__all__"
