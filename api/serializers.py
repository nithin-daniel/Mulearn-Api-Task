from rest_framework import serializers


class Login(serializers.Serializer):
    name = serializers.CharField(max_length=100) 
    password = serializers.CharField(max_length=100)