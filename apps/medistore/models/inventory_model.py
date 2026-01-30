from django.db import models
from apps.core.models.base_model import BaseModel

class Inventory(BaseModel):    
    medicine = models.OneToOneField(
        'medistore.Medicine',
        on_delete=models.CASCADE,
        related_name='inventory'
    )
    change_quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'inventory'

    def __str__(self):
        return f"{self.medicine.name} | Stock: {self.quantity}"
