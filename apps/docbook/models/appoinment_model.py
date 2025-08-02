from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import AppointmentStatus

class Appointment(BaseModel):
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_status = models.IntegerField(
        choices=[(status.value, status.name) for status in AppointmentStatus],
        default=AppointmentStatus.PENDING.value
    )
    patient = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='fk_patient_appointment_user_id'
    )
    doctor = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='fk_doctor_appointment_user_id'
    )
    
    notes = models.TextField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'appointment'
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        ordering = ['appointment_date']

    def __str__(self):
        return f"{self.patient.get_full_name()} - {self.doctor.user.get_full_name()} on {self.appointment_date}"
