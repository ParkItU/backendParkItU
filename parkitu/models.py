from django.db import models


class Cars(models.Model):
    carName = models.CharField(max_length=50)
    carOwner = models.CharField(max_length=50, )
    licensePlate = models.CharField(max_length=7)
    # carImage = models.ImageField(upload_to=)
    # date = models.DateField()
    firstTime = models.TimeField()
    lastTime = models.TimeField()

    def __str__(self):
        return self.carName

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Garages(models.Model):
    nameGarage = models.CharField(max_length=100)
    # imageGarage = models.ImageField(upload_to=)
    adressGarage = models.CharField(
        max_length=200, blank=True, null=True
    )

    def __str__(self):
        return self.nameGarage

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garages"
