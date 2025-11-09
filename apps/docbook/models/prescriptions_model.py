from django.db import models
from apps.core.models.base_model import BaseModel

class Prescription(BaseModel):
    appointment = models.OneToOneField(
        'docbook.Appointment',
        on_delete=models.CASCADE,
        related_name='fk_appointment_prescription_appointment_id'
    )
    doctor = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.CASCADE,
        related_name='fk_doctor_prescriptions_doctor_id'
    )
    patient = models.ForeignKey(
        'accounts.PatientProfile',
        on_delete=models.CASCADE,
        related_name='fk_patient_prescriptions_patient_id'
    )
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'prescriptions'
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescriptions'

    def __str__(self):
        return f"Prescription for {self.patient.get_full_name()} by {self.doctor.get_full_name()}"


