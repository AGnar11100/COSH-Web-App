# Generated by Django 5.1.5 on 2025-01-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsItem",
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
                ("image_url", models.URLField()),
                ("title", models.CharField(max_length=100)),
                ("summary", models.TextField()),
                ("detail_url", models.URLField()),
            ],
        ),
    ]
