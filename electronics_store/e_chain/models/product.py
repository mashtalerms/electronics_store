from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    model = models.CharField(blank=False, null=False, max_length=255)
    date_published = models.DateField(null=False, blank=False)

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")
        ordering = ["id"]

    def __str__(self):
        return self.title
