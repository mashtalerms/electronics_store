from rest_framework import serializers

from .models import Factory

#TODO сделать сериализаторы для всех подклассов и вставить их в общий BaseSer

class FactorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = "__all__"
