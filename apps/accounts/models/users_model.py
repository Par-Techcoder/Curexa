from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import Role
from apps.core.utilities.id_generator import generate_user_ids

class User(BaseModel, AbstractUser):
    public_id = models.CharField(
        max_length=35,
        unique=True,
        editable=False,
        db_index=True
    )

    middle_name = models.CharField(max_length=55, blank=True, null=True)

    role = models.IntegerField(
        choices=[(role.value, role.name) for role in Role],
        default=Role.PATIENT.value
    )

    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        # First save → get ID
        super().save(*args, **kwargs)

        # Second save → generate public_id
        if is_new and not self.public_id:            
            self.public_id = generate_user_ids(self.id, self.role)

            super().save(update_fields=["public_id"])

    def __str__(self):
        return f"{self.public_id} | {self.get_full_name()} | {self.email}"
