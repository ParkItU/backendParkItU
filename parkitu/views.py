from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from parkitu.models import Car, Garage
from parkitu.serializers import CarSerializer, GarageSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# class CarsInGarageViewSet(ModelViewSet):
#     queryset = CarsInGarage.objects.all()
#     serializer_class = CarsInGarageSerializer


class GarageViewSet(ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
