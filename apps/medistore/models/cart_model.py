from django.db import models
from apps.core.models.base_model import BaseModel

class Cart(BaseModel):    
    cart_owner = models.ForeignKey(
        'accounts.PatientProfile',
        on_delete=models.CASCADE, 
        related_name='fk_cart_owner_cart_ppatient_id'
    )

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f"{self.id} | User: {self.cart_owner.get_full_name()}"
