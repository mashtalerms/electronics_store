from .base import BaseModelMixin
from django.utils.translation import gettext_lazy as _


class Retail(BaseModelMixin):

    class Meta:
        verbose_name = _("Крупная розничная сеть")
        verbose_name_plural = _("Крупные розничные сети")
        ordering = ["id"]
