from django.db import models
from django.utils import timezone

#TODO Сделать как Json поля или как отдельные классы?

# class Address(models1.Model):
#     country = models1.CharField(max_length=40, null=False, blank=False)
#     city = models1.CharField(max_length=40, null=False, blank=False)
#     street = models1.CharField(max_length=40, null=False, blank=False)
#     house_number = models1.IntegerField(null=False, blank=False)
#
#
# class Contacts(models1.Model):
#     email = models1.CharField(max_length=40, null=False, blank=False)
#     address = models1.ForeignKey(Address, on_delete=models1.CASCADE)
#
#
# class Products(models1.Model):
#     title = models1.CharField(blank=False, null=False, max_length=255)
#     model = models1.CharField(blank=False, null=False, max_length=255)
#     date_published = models1.DateField(null=False, blank=False)


class BaseModelMixin(models.Model):

    # class Meta:
    #     abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    title = models.CharField(blank=False, null=False, max_length=255)
    contacts = models.JSONField()
    products = models.JSONField()
    staff = models.JSONField()
    debt = models.FloatField()
    created = models.DateTimeField(verbose_name="Дата создания")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)
