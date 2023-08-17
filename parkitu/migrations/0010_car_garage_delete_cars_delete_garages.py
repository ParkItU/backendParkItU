# Generated by Django 4.2.4 on 2023-08-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("parkitu", "0009_alter_cars_carname_alter_cars_carowner_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("carName", models.CharField(max_length=255)),
                ("carOwner", models.CharField(max_length=50)),
                ("licensePlate", models.CharField(max_length=7)),
                ("dateTime", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Car",
                "verbose_name_plural": "Cars",
            },
        ),
        migrations.CreateModel(
            name="Garage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nameGarage", models.CharField(max_length=255)),
                (
                    "adressGarage",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "verbose_name": "Garage",
                "verbose_name_plural": "Garages",
            },
        ),
        migrations.DeleteModel(
            name="Cars",
        ),
        migrations.DeleteModel(
            name="Garages",
        ),
    ]