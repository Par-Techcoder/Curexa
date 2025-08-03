from django.db import models
from apps.core.models.base_model import BaseModel

class InvoiceModel(BaseModel):
    order = models.ForeignKey(
        'orders.Order', on_delete=models.CASCADE, related_name='fk_orders_invoices_order_id'
    )
    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='fk_user_invoices_user_id'
    )

    invoice_number = models.CharField(max_length=20, unique=True)
    billing_address = models.TextField(null=True, blank=True)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    issued_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'invoices'
        ordering = ['-issued_at']

    def __str__(self):
        return f"Invoice #{self.invoice_number} for Order #{self.order_id}"
