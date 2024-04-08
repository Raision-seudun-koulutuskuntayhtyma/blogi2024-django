# Generated by Django 5.0.4 on 2024-04-08 10:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Postaus",
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
                ("otsikko", models.CharField(max_length=200)),
                ("teksti", models.TextField()),
                ("luotu", models.DateTimeField(auto_now_add=True)),
                ("viimeksi_muokattu", models.DateTimeField(auto_now=True)),
                ("julkaisuaika", models.DateTimeField(blank=True, null=True)),
                (
                    "kirjoittaja",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
