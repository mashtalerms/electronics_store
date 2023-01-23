from rest_framework.viewsets import ModelViewSet

from ..models.contact import Contact
from ..permissions import IsActiveUser
from ..serializers.contact import ContactSerializer, ContactCreateSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActiveUser]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ContactSerializer

        if self.action == "create" or self.action == "partial_update":
            return ContactCreateSerializer

        return super().get_serializer_class()
