# Generated by Django 4.1 on 2023-02-03 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0003_alter_book_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
