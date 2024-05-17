# Generated by Django 4.2.3 on 2024-05-17 00:08

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[utils.validators.validate_name],
                    ),
                ),
            ],
        ),
    ]
