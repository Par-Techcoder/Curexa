from django.db import models
from apps.core.models.base_model import BaseModel

class CartItem(BaseModel):
    medicine = models.ForeignKey(
        'medistore.Medicine', 
        on_delete=models.CASCADE, 
        related_name='fk_medicine_cart_items_medicine_id'
    )
    quantity = models.PositiveIntegerField(default=1)
    cart_owner = models.ForeignKey(
        'accounts.PatientProfile',
        on_delete=models.CASCADE, 
        related_name='fk_performed_cart_items_ppatient_id'
    )

    class Meta:
        db_table = 'cart_items'
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return f"{self.medicine.name} | Quantity: {self.quantity} | User: {self.cart_owner.get_full_name()}"
