from django.contrib import admin

from parkitu.models import Car, CarsInGarage, Garage

admin.site.register(CarsInGarage)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # list_display = ('garage_garageAdress', 'garage_garageName')
    search_fields = ("garage_garageAdress", "garage_garageName")
    # list_filter = ('garage_garageName', 'garage_garageAdress')
    # ordering = ('garage_garageName', 'garage_garageAdress')
    list_per_page = 25


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    # list_display = ('car_carName', 'car_licensePlate', 'car_dateTime')
    search_fields = ("car_carName", "car_licensePlate", "car_dateTime")
    # list_filter = ('car')
    # ordering = ('car_carName', 'car_licensePlate', 'car_dateTime')
    list_per_page = 25
