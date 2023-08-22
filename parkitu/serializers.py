from rest_framework.serializers import ModelSerializer

from parkitu.models import Car, Garage, CarsInGarage


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarsInGarageSerializer(ModelSerializer):
    class Meta:
        model = CarsInGarage
        fields = "__all__"


class GarageSerializer(ModelSerializer):
    class Meta:
        model = Garage
        fields = "__all__"
