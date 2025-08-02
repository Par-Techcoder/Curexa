from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import Role

class User(BaseModel, AbstractUser):
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    role = models.IntegerField(
        choices=[(role.value, role.name) for role in Role], 
        null=False, blank=False, default=Role.PATIENT.value
    )
    email = models.EmailField(max_length=255, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"ID: {self.id} | Name: {self.get_full_name()} | Email: {self.email} | Active: {self.is_active}"
