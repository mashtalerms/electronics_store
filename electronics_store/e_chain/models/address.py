from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    country = models.CharField(max_length=40, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    street = models.CharField(max_length=40, null=False, blank=False)
    house_number = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = _("Адрес")
        verbose_name_plural = _("Адреса")
        ordering = ["id"]

    def __str__(self):
        return self.country
