# Generated by Django 5.2.4 on 2025-07-31 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("isbn", models.CharField(max_length=13, unique=True)),
                ("published_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
