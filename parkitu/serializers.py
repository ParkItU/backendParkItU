from rest_framework.serializers import ModelSerializer

from parkitu.models import Cars


class CarsSerializer(ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"
