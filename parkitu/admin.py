from django.contrib import admin

from parkitu.models import Car, CarsInGarage, Garage

admin.site.register(Car)
admin.site.register(CarsInGarage)
admin.site.register(Garage)
