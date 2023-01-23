from django.utils import timezone

from django.db import models

from .contact import Contact
from .product import Product
# from common.models import BaseModel


class BaseModelMixin(models.Model):

    class Supplier(models.IntegerChoices):
        factory = 1, "Завод"
        distributor = 2, "Дистрибьютор"
        dealership = 3, "Дилерский центр"
        retail = 4, "Крупная розничная сеть"
        entrepreneur = 5, "Индивидуальный предприниматель"

    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    title = models.CharField(blank=False, null=False, max_length=255)
    staff = models.IntegerField(blank=True, null=True)
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    debt = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(verbose_name="Дата создания", blank=True, null=True)
    supplier = models.PositiveSmallIntegerField(
        verbose_name="Поставщик", choices=Supplier.choices, null=True
    )
    supplier_id = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

#TODO понять как сделать ссылку на suplier