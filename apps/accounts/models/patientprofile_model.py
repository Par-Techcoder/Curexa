from django.db import models
from apps.accounts.models.users_model import User
from apps.core.models.address_model import AddressModel
from apps.core.constants.default_values import Gender


class PatientProfile(AddressModel):
    patient = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    dob = models.DateField(blank=True, null=True)
    gender = models.IntegerField(
        choices=[(gender.value, gender.name) for gender in Gender],
        null=True,
        blank=True
    )
    profile_picture = models.ImageField(
        upload_to='static/images/profile_pictures/',
        blank=True,
        null=True
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'patients'
        verbose_name = 'Patient Profile'
        verbose_name_plural = 'Patient Profiles'

    def __str__(self):
        return f"Profile of {self.patient.get_full_name()} | Email: {self.patient.email} | Active: {self.patient.is_active}"
