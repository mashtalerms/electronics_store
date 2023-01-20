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


class FactoryCreateSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True, many=True)
    products = ProductsSerializer(read_only=True, many=True)
    staff = StaffSerializer(read_only=True, many=True)

    def create(self, validated_data):
        contacts = validated_data.pop("contacts", None)
        products = validated_data.pop("products", None)
        staff = validated_data.pop("staff", None)

        factory, _ = Factory.objects.get_or_create(**validated_data)

        if factory:

            for contact in contacts:

                if contact == "address":
                    for item in contact:
                        item, _ = Address.objects.get_or_create(**item)
                        contact.address.add(item)

                contact, _ = Contacts.objects.get_or_create(**contact)
                factory.contacts.add(contact)

            for product in products:
                product, _ = Products.objects.get_or_create(**product)
                factory.products.add(product)

            for person in staff:
                person, _ = Staff.objects.get_or_create(**person)
                factory.staff.add(person)

        return factory

    class Meta:
        model = Factory
        fields = "__all__"


# class FactorySerializer(BaseCreateSerializer):
#     class Meta:
#         model = Factory
#         fields = "__all__"
