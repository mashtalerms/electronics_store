from django.db import models

from electronics_store.e_chain.models.base import BaseModelMixin
from electronics_store.e_chain.models.dealership import Dealership


class Retail(BaseModelMixin):
    supplier = models.ForeignKey(Dealership, on_delete=models.CASCADE)
