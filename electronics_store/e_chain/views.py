from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Factory
from .serializers import FactoryCreateSerializer


# class FactoryViewSet(ModelViewSet):
#     queryset = Factory.objects.all()
#     serializer_class = FactorySerializer
#
#     d


class FactoryCreateView(APIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryCreateSerializer

    def post(self, request):
        factory_serializer = FactoryCreateSerializer(data=request.data, many=True)

        if factory_serializer.is_valid():
            # for item in request.data:
            factory_serializer = FactoryCreateSerializer(data=request.data)
            factory_serializer.is_valid(raise_exception=True)
            factory_serializer.save()
            return Response("Created successfully", status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": factory_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


