from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import PaymentStatus, PaymentMethod

class Payment(BaseModel):
    transaction_id = models.CharField(max_length=100, unique=True, editable=False)
    invoice = models.ForeignKey('InvoiceModel', on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.IntegerField(
        choices=[(method.value, method.name) for method in PaymentMethod]
    )
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in PaymentStatus],
        default=PaymentStatus.PENDING.value
    )

    class Meta:
        db_table = 'payments'
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ['-created_at']

    def __str__(self):
        return f"Payment {self.transaction_id} for Invoice {self.invoice.invoice_number} - Amount: {self.amount} - Status: {self.status}"
