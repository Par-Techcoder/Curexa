from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import OrderStatus

class Order(BaseModel):
    customer = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='fk_orders_orders_user_id')
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.IntegerField(
        choices=[(status, status.value) for status in OrderStatus ],
        default=OrderStatus.PROCESSING.value,
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount")

    class Meta:
        db_table = 'orders'
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-order_date']

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"
    
