from django.db import models
from apps.core.models.base_model import BaseModel

class OrderItem(BaseModel):
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='fk_order_items_order_order_id'
    )
    medicine = models.ForeignKey(
        'medistore.Medicine',
        on_delete=models.CASCADE,
        related_name='fk_order_items_medicine_medicine_id'
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_items'
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity} in Order #{self.order.id}"

    @property
    def total_price(self):
        return self.quantity * self.price
