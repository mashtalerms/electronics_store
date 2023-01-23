from rest_framework import serializers

from ..models.factory import Factory
from .contact import ContactSerializer
from .product import ProductSerializer


class FactoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer()

    class Meta:
        model = Factory
        fields = "__all__"
