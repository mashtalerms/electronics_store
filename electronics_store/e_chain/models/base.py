from django.utils import timezone

from django.db import models

from .contact import Contact
from .product import Product


class BaseModelMixin(models.Model):

    class Supplier(models.IntegerChoices):
        empty = 99, ""
        factory = 0, "Завод"
        distributor = 1, "Дистрибьютор"
        dealership = 2, "Дилерский центр"
        retail = 3, "Крупная розничная сеть"
        entrepreneur = 4, "Индивидуальный предприниматель"

    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД
        ordering = ["-id"]

    title = models.CharField(blank=False, null=False, max_length=255)
    staff = models.IntegerField(blank=True, null=True)
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    debt = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(verbose_name="Дата создания", blank=True, null=True)
    chain_position = models.SmallIntegerField(verbose_name="Уровень иерархии", null=True)
    supplier = models.PositiveSmallIntegerField(
        verbose_name="Поставщик", choices=Supplier.choices, null=True
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
