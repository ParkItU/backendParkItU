# Generated by Django 4.2.4 on 2023-08-22 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("parkitu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="imageCar",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]