# Generated by Django 4.0.4 on 2022-06-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0003_movie_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
