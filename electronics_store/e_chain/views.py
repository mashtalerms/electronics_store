from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Factory
from .serializers import FactorySerializer


class FactoryViewSet(ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
