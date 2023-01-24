from .base import BaseModelMixin


class Dealership(BaseModelMixin):

    class Meta:
        verbose_name = "Дилерский центр"
        verbose_name_plural = "Дилерские центры"
        ordering = ["id"]

