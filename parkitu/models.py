from django.db import models


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    carName = models.CharField(max_length=255)
    carOwner = models.CharField(
        max_length=50,
    )
    licensePlate = models.CharField(max_length=7)
    dateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.licensePlate} ({self.dateTime})"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Garage(models.Model):
    nameGarage = models.CharField(max_length=255)
    adressGarage = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nameGarage} ({self.adressGarage})"

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garages"
