from django.db import models
from apps.core.models.base_model import BaseModel

class Inventory(BaseModel):    
    medicine = models.OneToOneField(
        'medistore.Medicine',
        on_delete=models.CASCADE,
        related_name='inventory'
    )
    quantity = models.PositiveIntegerField()
    stock_alert_level = models.IntegerField(default=0)

    class Meta:
        db_table = 'inventory'

    def __str__(self):
        return f"{self.medicine.name} | Stock: {self.quantity}"
