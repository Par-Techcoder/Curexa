from django.db import models
from apps.core.models.base_model import BaseModel

class Orders(BaseModel):
    order_id = models.CharField(max_length=100, unique=True, verbose_name="Order ID")
    customer_name = models.CharField(max_length=255, verbose_name="Customer Name")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Order Date")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount")

    class Meta:
        db_table = 'orders'
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-order_date']

    def __str__(self):
        return f"Order {self.order_id} by {self.customer_name}"
    
