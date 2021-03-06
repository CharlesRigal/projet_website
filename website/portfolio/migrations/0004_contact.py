# Generated by Django 3.1.4 on 2021-01-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_cv"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=100, verbose_name="Objet")),
                ("message", models.TextField(verbose_name="message")),
            ],
        ),
    ]
