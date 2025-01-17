# Generated by Django 5.1.4 on 2025-01-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=50)),
                ("pricde", models.IntegerField()),
                ("description", models.TextField()),
                ("quntity", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=20)),
                ("age", models.IntegerField(default=0)),
                ("email", models.EmailField(max_length=100)),
                ("address", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("file", models.FileField(upload_to="")),
                ("dob", models.DateField()),
            ],
        ),
    ]
