from django.db import models
from django.utils import timezone


class Address(models.Model):
    country = models.CharField(max_length=40, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    street = models.CharField(max_length=40, null=False, blank=False)
    house_number = models.IntegerField(null=False, blank=False)


class Contacts(models.Model):
    email = models.CharField(max_length=40, null=False, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Products(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    model = models.CharField(blank=False, null=False, max_length=255)
    date_published = models.DateField(null=False, blank=False)


class Staff(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    is_active = models.BooleanField(default=False)


class BaseModelMixin(models.Model):

    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    title = models.CharField(blank=False, null=False, max_length=255)
    contacts = models.ManyToManyField(Contacts, blank=True, null=True)
    products = models.ManyToManyField(Products, blank=True, null=True)
    staff = models.ManyToManyField(Staff, blank=True, null=True)
    debt = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(verbose_name="Дата создания", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class Factory(BaseModelMixin):

    class Meta:
        verbose_name = "Фабрика"
        verbose_name_plural = "Фабрики"


class Distributor(BaseModelMixin):
    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Дистрибьютор"
        verbose_name_plural = "Дистрибьюторы"


class Dealership(BaseModelMixin):
    supplier = models.ForeignKey(Distributor, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Дилерский центр"
        verbose_name_plural = "Дилерские центры"


class Retail(BaseModelMixin):
    supplier = models.ForeignKey(Dealership, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Крупная розничная сеть"
        verbose_name_plural = "Крупные розничные сети"


class Entrepreneur(BaseModelMixin):
    supplier = models.ForeignKey(Retail, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
