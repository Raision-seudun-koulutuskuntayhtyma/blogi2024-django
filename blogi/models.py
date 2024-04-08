from django.conf import settings
from django.db import models


class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField()

    kirjoittaja = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
    )
    luotu = models.DateTimeField(auto_now_add=True)
    viimeksi_muokattu = models.DateTimeField(auto_now=True)
    julkaisuaika = models.DateTimeField(null=True, blank=True)
