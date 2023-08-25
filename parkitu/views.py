from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from parkitu.models import Car, CarsInGarage, Garage
from parkitu.serializers import (
    CarDetailSerializer,
    CarListSerializer,
    CarSerializer,
    CarsInGarageSerializer,
    GarageDetailSerializer,
    GarageListSerializer,
    GarageSerializer,
)


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CarListSerializer
        elif self.action == "retrieve":
            return CarDetailSerializer
        return CarSerializer


class CarsInGarageViewSet(ModelViewSet):
    queryset = CarsInGarage.objects.all()
    serializer_class = CarsInGarageSerializer


class GarageViewSet(ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return GarageListSerializer
        elif self.action == "retrieve":
            return GarageDetailSerializer
        return GarageSerializer
