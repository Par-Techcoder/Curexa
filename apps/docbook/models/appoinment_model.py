from django.db import models
from apps.core.models.base_model import BaseModel

class Appoinment(BaseModel):
    appointment_date = models.DateTimeField(verbose_name="Appointment Date")
    patient_name = models.CharField(max_length=255, verbose_name="Patient Name")
    doctor_name = models.CharField(max_length=255, verbose_name="Doctor Name")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    class Meta:
        db_table = 'appointment'
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        ordering = ['appointment_date']

    def __str__(self):
        return f"{self.patient_name} - {self.doctor_name} on {self.appointment_date}"

