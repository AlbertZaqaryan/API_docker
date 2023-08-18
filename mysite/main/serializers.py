from rest_framework import serializers
from .models import Car, Phone

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'price', 'year']



class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['name', 'price']