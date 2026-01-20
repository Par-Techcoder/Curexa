from django.contrib.auth.models import BaseUserManager
from apps.core.constants.default_values import Role


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        first_name="",
        middle_name="",
        last_name="",
        password=None,
        role=Role.PATIENT.value,
    ):
        if not email:
            raise ValueError("Email must be provided")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            role=role,
        )

        user.set_password(password or self.make_random_password())
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=email,
            password=password,
            role=Role.ADMIN.value,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
