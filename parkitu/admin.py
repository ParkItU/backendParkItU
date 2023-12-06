from django.contrib import admin

from parkitu.models import Car, Garage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "ownerPhone",
        "licensePlate",
        "date",
    )
    search_fields = (
        "name",
        "owner",
        "ownerPhone",
        "licensePlate",
        "date",
    )
    list_filter = (
        "name",
        "owner",
        "ownerPhone",
        "licensePlate",
        "date",
    )
    ordering = (
        "name",
        "owner",
        "ownerPhone",
        "licensePlate",
        "date",
    )
    list_per_page = 25


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address")
    list_filter = ("name", "address")
    ordering = ("name", "address")

    list_per_page = 25
