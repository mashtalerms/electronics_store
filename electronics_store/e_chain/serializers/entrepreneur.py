from rest_framework import serializers

from ..models.entrepreneur import Entrepreneur
from .contact import ContactSerializer
from .product import ProductSerializer


class EntrepreneurCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entrepreneur
        fields = "__all__"


class EntrepreneurUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = "__all__"
        read_only_fields = ('debt',)


class EntrepreneurSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer()

    class Meta:
        model = Entrepreneur
        fields = "__all__"
