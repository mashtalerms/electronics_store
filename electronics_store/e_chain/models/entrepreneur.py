from .base import BaseModelMixin


class Entrepreneur(BaseModelMixin):

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
        ordering = ["id"]
