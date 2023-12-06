from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from parkitu.models import Car, Garage
from uploader.models import Image
from uploader.serializers import ImageSerializer


class GarageSerializer(serializers.ModelSerializer):
    image_attachment_key = serializers.SlugRelatedField(
        source="image",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image = ImageSerializer(required=False, read_only=True)
    cars = serializers.SerializerMethodField(source="get_cars")

    class Meta:
        model = Garage
        fields = ("id", "name", "address", "image", "image_attachment_key", "cars")

    def get_cars(self, obj):
        return [car.name for car in obj.car_set.all()]


class GarageDetailSerializer(ModelSerializer):
    image = ImageSerializer(required=False)
    cars = GarageSerializer(many=True)

    class Meta:
        model = Garage
        fields = ("id", "name", "address", "image", "cars")


class CarSerializer(serializers.ModelSerializer):
    image_attachment_key = serializers.SlugRelatedField(
        source="image",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image = ImageSerializer(required=False, read_only=True)
    garage = SlugRelatedField(queryset=Garage.objects.all(), slug_field="name")

    def get_garage(self, obj):
        return obj.garage.name

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "owner",
            "ownerPhone",
            "licensePlate",
            "image",
            "date",
            "garage",
            "image_attachment_key",
        )


class CarListSerializer(ModelSerializer):
    image = ImageSerializer(required=False)

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "owner",
            "ownerPhone",
            "licensePlate",
            "image",
            "date",
            "garage",
        )
