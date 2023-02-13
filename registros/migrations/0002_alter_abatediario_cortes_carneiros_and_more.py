# Generated by Django 4.1.5 on 2023-01-25 16:34

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registros", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="abatediario",
            name="cortes_carneiros",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0.0)]
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="abatediario",
            name="cortes_suinos",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0.0)]
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="cortes_carneiros",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0.0)]
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="cortes_suinos",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0.0)]
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]