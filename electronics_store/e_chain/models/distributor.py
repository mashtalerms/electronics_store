from .base import BaseModelMixin
from django.db import models


class Distributor(BaseModelMixin):

    class Meta:
        verbose_name = "Дистрибьютор"
        verbose_name_plural = "Дистрибьюторы"
        ordering = ["id"]

