from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from parkitu.models import Car, CarsInGarage, Garage
from uploader.models import Image
from uploader.serializers import ImageSerializer


class CarSerializer(ModelSerializer):
    image_attachment_key = SlugRelatedField(
        source="image",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Car
        fields = "__all__"


class CarDetailSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        depth = 1
        image = ImageSerializer(required=False)


class CarListSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarsInGarageSerializer(ModelSerializer):
    class Meta:
        model = CarsInGarage
        fields = "__all__"


class GarageSerializer(ModelSerializer):
    image_attachment_key = SlugRelatedField(
        source="image",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Garage
        fields = ("id", "nameGarage", "adressGarage", "image", "image_attachment_key")


class GarageDetailSerializer(ModelSerializer):
    image = CharField(source="image.url")

    class Meta:
        model = Garage
        fields = ("id", "nameGarage", "adressGarage", "image")


class GarageListSerializer(ModelSerializer):
    image = CharField(source="image.url")

    class Meta:
        model = Garage
        fields = ["nameGarage", "adressGarage", "image"]
