from django.db import models

from electronics_store.e_chain.models.base import BaseModelMixin
from electronics_store.e_chain.models.factory import Factory


class Distributor(BaseModelMixin):
    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE)
