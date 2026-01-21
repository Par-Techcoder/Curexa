from apps.accounts.models import User
from apps.core.constants.default_values import Role
import secrets
from django.core.mail import send_mail
from django.conf import settings

OTP_EXPIRY_SECONDS = 300  # 5 minutes
OTP_ATTEMPT_LIMIT = 5
OTP_SEND_LIMIT = 5
OTP_RESEND_COOLDOWN = 30  # seconds

def user_create_or_check(email):
    """
    Create a user if it doesn't exist or return the existing user.
    """
    user, created = User.objects.get_or_create(
        email=email,
        defaults={"username": email.split("@")[0]}
    )

    if created:
        user.set_password('12345')
        user.save()

    return user

def create_doctor_user(first_name, middle_name, last_name, email):
    """
    Create a user with doctor role.
    """
    user = User(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        email=email,        
        role=Role.DOCTOR.value,
    )
    temp_password = secrets.token_urlsafe(12)
    user.set_password(temp_password)
    send_mail(
        subject="Your Password for Doctor Account",
        message=f"Your temporary password is {temp_password}. Please log in and change your password.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )
    user.save()
    return user