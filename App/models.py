from django.db import models
from django.utils.timezone import now
import datetime


class Country(models.Model):
    country_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.country_name

    class Meta:
        ordering = ('-date_created', )
