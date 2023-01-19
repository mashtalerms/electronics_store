from django.db import models

from electronics_store.e_chain.models.base import BaseModelMixin
from electronics_store.e_chain.models.retail import Retail


class Entrepreneur(BaseModelMixin):
    supplier = models.ForeignKey(Retail, on_delete=models.CASCADE)
