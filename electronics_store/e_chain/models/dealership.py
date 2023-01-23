from .base import BaseModelMixin
from django.db import models


class Dealership(BaseModelMixin):

    class Meta:
        verbose_name = "Дилерский центр"
        verbose_name_plural = "Дилерские центры"
        ordering = ["id"]

