from .base import BaseModelMixin


class Distributor(BaseModelMixin):

    class Meta:
        verbose_name = "Дистрибьютор"
        verbose_name_plural = "Дистрибьюторы"
        ordering = ["id"]
