from .base import BaseModelMixin
from django.db import models


class Entrepreneur(BaseModelMixin):

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
