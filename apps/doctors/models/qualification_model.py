from django.db import models
from apps.core.models.base_model import BaseModel

class Qualification(BaseModel):
    doctor = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.CASCADE,
        related_name='fk_qualifications_doctor_profile_doctor_id'
    )
    degree = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    year_completed = models.DateField()

    class Meta:
        db_table = 'doctor_qualifications'
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"
        ordering = ['-year_completed']
        unique_together = ('doctor', 'degree', 'institute')

    def __str__(self):
        return f"Doctor: {self.doctor.doctor.get_full_name()} | Degree:{self.degree} | Active: {self.is_active}" # since doctor here refers to a DoctorProfile, whose doctor is the actual user