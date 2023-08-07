from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from parkitu.models import Cars
from parkitu.models import Garages
from parkitu.models import Details

from parkitu.serializers import CarsSerializer
from parkitu.serializers import GaragesSerializer
from parkitu.serializers import DetailsSerializer


class CarsViewSet(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class GaragesViewSet(ModelViewSet):
    queryset = Garages.objects.all()
    serializer_class = GaragesSerializer


class DetailsViewSet(ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
