from .base import BaseModelMixin
from django.utils.translation import gettext_lazy as _


class Factory(BaseModelMixin):

    class Meta:
        verbose_name = _("Фабрика")
        verbose_name_plural = _("Фабрики")
        ordering = ["id"]
