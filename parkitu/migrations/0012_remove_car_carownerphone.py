# Generated by Django 4.2.7 on 2023-11-13 13:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("parkitu", "0011_alter_car_carownerphone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="carOwnerPhone",
        ),
    ]
