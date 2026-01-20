from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import Role
from apps.core.utilities.id_generator import generate_user_ids
from apps.core.utilities.user_manager import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    public_id = models.CharField(
        max_length=35,
        unique=True,
        editable=False,
        db_index=True
    )

    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    last_name = models.CharField(max_length=55)

    role = models.IntegerField(
        choices=[(r.value, r.name) for r in Role],
        default=Role.PATIENT.value
    )
    
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        # First save → get ID
        super().save(*args, **kwargs)

        # Second save → generate public_id
        if is_new and not self.public_id:
            self.public_id = generate_user_ids(self.id, self.role)
            super().save(update_fields=["public_id"])

    def get_full_name(self):
        return " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))

    def __str__(self):
        return f"{self.public_id} | {self.email}"
