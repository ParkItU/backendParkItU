from django.db import models

from uploader.models import Image


class Car(models.Model):
    carName = models.CharField(max_length=255)
    carOwner = models.CharField(
        max_length=50,
    )
    licensePlate = models.CharField(max_length=7)
    dateTime = models.DateTimeField(auto_now=True)
    imageCar = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.carName} ({self.carOwner} {self.licensePlate} {self.dateTime})"


class Garage(models.Model):
    nameGarage = models.CharField(max_length=255)
    adressGarage = models.CharField(max_length=255, blank=True, null=True)
    imageGarage = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.nameGarage} ({self.adressGarage})"

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garages"


class CarsInGarage(models.Model):
    idCar = models.ManyToManyField(Car)
    idGarage = models.ForeignKey(
        Garage, on_delete=models.CASCADE, default=0, related_name="carInGarage"
    )

    def __str__(self):
        return f"{self.idCar} ({self.idGarage})"

    class Meta:
        verbose_name = "CarsInGarage"
        verbose_name_plural = "CarsInGarages"
