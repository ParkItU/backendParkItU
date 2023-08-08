from rest_framework.serializers import ModelSerializer

from parkitu.models import Cars, Garages


class CarsSerializer(ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"


class GaragesSerializer(ModelSerializer):
    class Meta:
        model = Garages
        fields = "__all__"
