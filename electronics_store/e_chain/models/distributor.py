from .base import BaseModelMixin
from django.utils.translation import gettext_lazy as _


class Distributor(BaseModelMixin):

    class Meta:
        verbose_name = _("Дистрибьютор")
        verbose_name_plural = _("Дистрибьюторы")
        ordering = ["id"]
