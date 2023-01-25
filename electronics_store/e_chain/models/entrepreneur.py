from .base import BaseModelMixin
from django.utils.translation import gettext_lazy as _


class Entrepreneur(BaseModelMixin):

    class Meta:
        verbose_name = _("Индивидуальный предприниматель")
        verbose_name_plural = _("Индивидуальные предприниматели")
        ordering = ["id"]
