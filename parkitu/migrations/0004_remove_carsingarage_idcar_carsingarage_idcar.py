# Generated by Django 4.2.4 on 2023-08-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("parkitu", "0003_garage_imagegarage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carsingarage",
            name="idCar",
        ),
        migrations.AddField(
            model_name="carsingarage",
            name="idCar",
            field=models.ManyToManyField(to="parkitu.car"),
        ),
    ]
