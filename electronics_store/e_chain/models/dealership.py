from .base import BaseModelMixin
from django.utils.translation import gettext_lazy as _


class Dealership(BaseModelMixin):

    class Meta:
        verbose_name = _("Дилерский центр")
        verbose_name_plural = _("Дилерские центры")
        ordering = ["id"]

