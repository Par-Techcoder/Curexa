from django.db import models
from apps.core.models.base_model import BaseModel

class Qualification(BaseModel):
    doctor = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.CASCADE,
        related_name='fk_qualifications_doctor_profile_doctor_id'
    )
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    completion_year = models.DateField()

    class Meta:
        db_table = 'doctor_qualifications'
        ordering = ['-completion_year']
        unique_together = ('doctor', 'degree', 'institution')

    def __str__(self):
        return f"Doctor: {self.doctor.doctor.get_full_name()} | Degree:{self.degree} | Active: {self.is_active}" # since doctor here refers to a DoctorProfile, whose doctor is the actual user