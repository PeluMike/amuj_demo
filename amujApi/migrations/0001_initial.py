# Generated by Django 4.2.6 on 2023-10-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Collections",
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
                ("title", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300, unique=True)),
                ("description", models.TextField()),
                ("createdOn", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
