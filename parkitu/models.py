from django.db import models

from uploader.models import Image


class Car(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=50)
    ownerPhone = models.CharField(max_length=11)
    licensePlate = models.CharField(max_length=7)
    date = models.DateField()
    image = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    garage = models.ForeignKey("Garage", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.owner}) ({self.ownerPhone}) ({self.licensePlate}) ({self.date}) ({self.image}) ({self.garage})"


class Garage(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    # car = models.ManyToManyField(Car)

    def __str__(self):
        return f"{self.name} ({self.address}) ({self.image})"

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garages"
