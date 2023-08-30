from rest_framework.serializers import ModelSerializer, SlugRelatedField

from parkitu.models import Car, CarsInGarage, Garage
from uploader.models import Image
from uploader.serializers import ImageSerializer


class CarSerializer(ModelSerializer):
    imageCar_attachment_key = SlugRelatedField(
        source="imageCar",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imageCar = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Car
        fields = "__all__"


class CarDetailSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        depth = 1
        imageCar = ImageSerializer(required=False)


class CarListSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarsInGarageSerializer(ModelSerializer):
    class Meta:
        model = CarsInGarage
        fields = "__all__"


class GarageSerializer(ModelSerializer):
    imageGarage_attachment_key = SlugRelatedField(
        source="imageGarage",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imageGarage = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Garage
        fields = "__all__"


class GarageDetailSerializer(ModelSerializer):
    class Meta:
        model = Garage
        fields = "__all__"
        depth = 1
        imageGarage = ImageSerializer(required=False)


class GarageListSerializer(ModelSerializer):
    class Meta:
        model = Garage
        fields = ["nameGarage", "adressGarage"]
