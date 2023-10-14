# Generated by Django 4.2.6 on 2023-10-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("amujApi", "0003_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Size",
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
                ("size", models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.ManyToManyField(blank=True, to="amujApi.size"),
        ),
    ]
