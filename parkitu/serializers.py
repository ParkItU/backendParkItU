from rest_framework.serializers import ModelSerializer

from parkitu.models import Cars
from parkitu.models import Garages
from parkitu.models import Details


class CarsSerializer(ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"


class GaragesSerializer(ModelSerializer):
    class Meta:
        model = Garages
        fields = "__all__"


class DetailsSerializer(ModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"
