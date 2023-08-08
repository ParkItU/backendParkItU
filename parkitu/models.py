from django.db import models


class Cars(models.Model):
    carName = models.CharField(max_length=50, default="Nome do Carro")
    carOwner = models.CharField(max_length=50, default="Dono do Carro")
    licensePlate = models.CharField(max_length=7, default="PLaca do Carro")
    # carImage = models.ImageField(upload_to=)
    # date = models.DateField()
    firstTime = models.TimeField(default="Horário de entrada")
    lastTime = models.TimeField(default="Horário de Saída")

    def __str__(self):
        return self.carName

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Garages(models.Model):
    nameGarage = models.CharField(max_length=100, default="Nome da Garagem")
    # imageGarage = models.ImageField(upload_to=)
    adressGarage = models.CharField(max_length=200, blank=True, null=True, default="Endereço da Garagem")

    def __str__(self):
        return self.nameGarage

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garages"