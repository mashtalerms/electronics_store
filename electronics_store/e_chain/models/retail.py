from .base import BaseModelMixin


class Retail(BaseModelMixin):

    class Meta:
        verbose_name = "Крупная розничная сеть"
        verbose_name_plural = "Крупные розничные сети"
        ordering = ["id"]
