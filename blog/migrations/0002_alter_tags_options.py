# Generated by Django 4.1 on 2023-02-22 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tags",
            options={"verbose_name_plural": "Tags"},
        ),
    ]