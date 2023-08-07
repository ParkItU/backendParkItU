from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from parkitu.models import Cars
from parkitu.serializers import CarsSerializer


class CarsViewSet(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
