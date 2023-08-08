from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from parkitu.models import Cars, Garages
from parkitu.serializers import CarsSerializer, GaragesSerializer


class CarsViewSet(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class GaragesViewSet(ModelViewSet):
    queryset = Garages.objects.all()
    serializer_class = GaragesSerializer