# Generated by Django 4.2.7 on 2023-11-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("parkitu", "0010_alter_car_carownerphone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="carOwnerPhone",
            field=models.CharField(default="Seu-valor-padrão", max_length=15),
        ),
    ]