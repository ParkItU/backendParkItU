from django.db import models


class Cars(models.Model):
    carName = models.CharField(max_length=50)
    carOwner = models.CharField(max_length=50)
    # carImage = models.ImageField(upload_to=)

    def __str__(self):
        return self.carName

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Garages(models.Model):
    nameGarage = models.CharField(max_length=100)
    # imageGarage = models.ImageField(upload_to=)

    def __str__(self):
        return self.nameGarage

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garages"


class Details(models.Model):
    carName = models.ForeignKey(
        Cars, on_delete=models.PROTECT, related_name="car_name_details"
    )
    carOwner = models.ForeignKey(
        Cars, on_delete=models.PROTECT, related_name="car_owner_details"
    )
    nameGarage = models.ForeignKey(
        Garages, on_delete=models.PROTECT, related_name="name_garage_details"
    )
    # carImage = models.ImageField(upload_to=)
    licensePlate = models.CharField(max_length=7)
    date = models.DateField()
    firstTime = models.TimeField()
    lastTime = models.TimeField()

    def __str__(self):
        return f"{self.firstTime} ({self.lastTime})"

    class Meta:
        verbose_name = "Detail"
        verbose_name_plural = "Details"
