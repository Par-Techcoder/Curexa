from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import TestBookingStatus

class TestBooking(BaseModel):

    patient = models.ForeignKey(
        'accounts.PatientProfile',
        on_delete=models.CASCADE,
        related_name='fk_patient_testbooking_patient_id'
    )
    test = models.ForeignKey(
        'labtests.MedicalTest',
        on_delete=models.CASCADE,
        related_name='fk_test_testbooking_test_id'
    )    
    booking_date = models.DateField()
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in TestBookingStatus],
        default=TestBookingStatus.PENDING.value
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'test_bookings'
        ordering = ['-booking_date']

    def __str__(self):
        return f"{self.patient.get_full_name()} - {self.test.name} on {self.booking_date}"