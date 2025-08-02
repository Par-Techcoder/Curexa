from django.db import models
from apps.accounts.models.users_model import User
from apps.core.models.address_model import AddressModel
from apps.core.constants.default_values import Gender

class Profile(User, AddressModel):
    dob = models.DateField(blank=True, null=True)
    gender = models.IntegerField(   
        choices=[(gender.value, gender.name) for gender in Gender]
    )
    profile_picture = models.ImageField(upload_to='static/images/profile_pictures/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"ID:{self.id}, Profile of {self.get_full_name()} | Email: {self.email} | Active: {self.is_active}"
