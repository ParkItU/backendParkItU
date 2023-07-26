from django.db import models


class Cars(models.Model):
    carName = models.CharField(max_length=50)
    carOwner = models.CharField(max_length=50)
    # carImage = models.ImageField(upload_to=)

    def __str__(self):
        return self.carName


class Details(models.Model):
    carName = models.CharField(max_length=50)
    carOwner = models.CharField(max_length=50)
    # carImage = models.ImageField(upload_to=)
    licensePlate = models.CharField(max_length=7)
    date = models.DateField()
    firstTime = models.TimeField()
    lastTime = models.TimeField()
    garageName = models.CharField(max_length=100)

    def __str__(self):
        return self.licensePlate


class Garages(models.Model):
    name = models.CharField(max_length=100)
    # imageGarage = models.ImageField(upload_to=)

    def __str__(self):
        return self.name
