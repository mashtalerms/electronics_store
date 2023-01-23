from rest_framework import serializers

from .address import AddressSerializer
from ..models.contact import Contact


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Contact
        fields = "__all__"
