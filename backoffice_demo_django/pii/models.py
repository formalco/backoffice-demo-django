from django.utils.translation import gettext_lazy as _
from django.db import models

class Pii(models.Model):
    first_name = models.TextField(blank=True, primary_key=True)
    last_name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    eu = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pii'
