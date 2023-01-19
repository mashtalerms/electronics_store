from rest_framework import serializers

from .models import Factory, Address, Contacts, Products, Staff, BaseModelMixin


#TODO сделать сериализаторы для всех подклассов и вставить их в общий BaseSer
#TODO переписать ser https://stackoverflow.com/questions/66116353/use-django-rest-framework-serializer-to-save-json-requests-to-database

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True, many=True)
    class Meta:
        model = Contacts
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class BaseSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True, many=True)
    products = ProductsSerializer(read_only=True, many=True)
    staff = StaffSerializer(read_only=True, many=True)

    class Meta:
        model = BaseModelMixin
        fields = "__all__"


class FactorySerializer(BaseSerializer):
    class Meta:
        model = Factory
        fields = "__all__"
