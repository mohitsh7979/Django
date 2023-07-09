from rest_framework import serializers
from .models import apimodel


class apiserializer(serializers.Serializer):

    name = serializers.CharField(max_length=30)
    f_name = serializers.CharField(max_length=30)
    mobile_no = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=50)