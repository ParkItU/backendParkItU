from django.db import models


class Car(models.Model):
    # id = models.BigAutoField(primary_key=True)
    carName = models.CharField(max_length=255)
    carOwner = models.CharField(
        max_length=50,
    )
    licensePlate = models.CharField(max_length=7)
    dateTime = models.DateTimeField(auto_now=True)
    # garageCar = models.ForeignKey(Garage, on_delete=models.PROTECT, related_name="car")

    def __str__(self):
        return f"{self.carName} ({self.carOwner} {self.licensePlate} {self.dateTime})"


class Garage(models.Model):
    # id = models.BigAutoField(primary_key=True)
    nameGarage = models.CharField(max_length=255)
    adressGarage = models.CharField(max_length=255, blank=True, null=True)
    # cars = models.ManyToManyField(Car, through="CarsInGarage")

    def __str__(self):
        return f"{self.nameGarage} ({self.adressGarage})"

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garages"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class CarsInGarage(models.Model):
    idCar = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name="carsInGarage"
    )
    idGarage = models.ForeignKey(
        Garage, on_delete=models.CASCADE, default=0, related_name="carInGarage"
    )

    def __str__(self):
       return f"{self.idCar} ({self.idGarage})"

    class Meta:
        verbose_name = "CarsInGarage"
        verbose_name_plural = "CarsInGarages"
