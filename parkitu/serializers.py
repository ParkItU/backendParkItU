from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SlugRelatedField


from uploader.models import Image
from uploader.serializers import ImageSerializer

from parkitu.models import Car, Garage, CarsInGarage


class CarSerializer(ModelSerializer):
    imageCar_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imageCar = ImageSerializer(required=False, read_only=True)
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
