from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import AppointmentType, AppointmentStatus

class Appointment(BaseModel):
    appointment_type = models.IntegerField(
        choices=[(status.value, status.name) for status in AppointmentType],
        default=AppointmentType.CONSULTATION.value
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_status = models.IntegerField(
        choices=[(status.value, status.name) for status in AppointmentStatus],
        default=AppointmentStatus.PENDING.value
    )
    patient = models.ForeignKey(
        'accounts.PatientProfile',
        on_delete=models.CASCADE,
        related_name='fk_patient_appointment_patient_id'
    )
    doctor = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.CASCADE,
        related_name='fk_doctor_appointments_doctor_id'
    )
    
    notes = models.TextField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'appointments'
        ordering = ['appointment_date']

    def __str__(self):
        return f"{self.patient.get_full_name()} - {self.doctor.get_full_name()} on {self.appointment_date}"
