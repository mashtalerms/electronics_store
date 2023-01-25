from django.db import models
from django.utils.translation import gettext_lazy as _
from .address import Address


class Contact(models.Model):
    email = models.CharField(max_length=40, null=False, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Контакт")
        verbose_name_plural = _("Контакты")
        ordering = ["id"]

    def __str__(self):
        return self.email
