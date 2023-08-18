from django.shortcuts import render
from rest_framework import viewsets
from .models import Car, Phone
from .serializers import CarSerializers, PhoneSerializers
# Create your views here.


class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers



class PhoneView(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers
    