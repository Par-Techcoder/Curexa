from apps.core.models.base_model import BaseModel
from django.db import models

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
