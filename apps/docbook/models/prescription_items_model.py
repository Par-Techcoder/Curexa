from django.db import models
from apps.core.models.base_model import BaseModel

class PrescriptionItem(BaseModel):
    prescription = models.ForeignKey(
        'docbook.Prescription',
        on_delete=models.CASCADE,
        related_name='fk_prescription_prescriptionitems_prescription_id'
    )
    medicine = models.ForeignKey(
        'medistore.Medicine',
        on_delete=models.CASCADE,
        related_name='fk_medicine_prescription_items_medicine_id'
    )
    quantity = models.PositiveIntegerField(default=1)
    dosage = models.CharField(max_length=255, blank=True, null=True)  # e.g., "1 tablet twice a day"
    duration = models.CharField(max_length=100, blank=True, null=True)  # e.g., "5 days"
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'prescription_items'
        verbose_name = 'Prescription Item'
        verbose_name_plural = 'Prescription Items'

    def __str__(self):
        return f"{self.medicine.name} - {self.dosage} for {self.duration}"
