# Generated by Django 4.2.6 on 2023-10-13 18:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("amujApi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collections",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
