from .base import BaseModelMixin
from django.db import models


class Retail(BaseModelMixin):

    class Meta:
        verbose_name = "Крупная розничная сеть"
        verbose_name_plural = "Крупные розничные сети"
