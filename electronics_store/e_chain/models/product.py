from django.db import models


class Product(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    model = models.CharField(blank=False, null=False, max_length=255)
    date_published = models.DateField(null=False, blank=False)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title
