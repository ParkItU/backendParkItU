from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from parkitu.models import Car
from parkitu.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
