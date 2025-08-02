from django.db import models
from apps.core.models.address_model import AddressModel

class DoctorProfile(AddressModel):
    doctor = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='fk_doctor_doctor_profile_user_id'
    )
    specialization = models.ForeignKey(
        'doctors.Specialization',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='fk_specialization_doctor_profile_specialization_id'
    )
    experience_years = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='static/images/doctor_profiles/', blank=True, null=True)
    
    class Meta:
        db_table = 'doctors'
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        ordering = ['doctor__first_name']
    
    def __str__(self):
        return f"Doctor: {self.doctor.get_full_name()} | Specialization: {self.specialization} | Active: {self.is_active}"
