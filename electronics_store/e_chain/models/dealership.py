from django.db import models

from electronics_store.e_chain.models.base import BaseModelMixin
from electronics_store.e_chain.models.distributor import Distributor


class Dealership(BaseModelMixin):
    supplier = models.ForeignKey(Distributor, on_delete=models.CASCADE)
