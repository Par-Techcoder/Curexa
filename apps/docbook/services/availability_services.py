from apps.docbook.models.availability_model import Availability
from django.utils import timezone
from datetime import timedelta


def check_doctor_availability(doctor, date, start_time):
    return Availability.objects.filter(
        doctor=doctor,
        date=date,
        start_time=start_time,
        is_available=True
    ).exists()

def today_doctor_availabilities(doctor):
    today = timezone.localdate()
    return Availability.objects.filter(
        doctor=doctor,
        date=today,
        is_available=True
    )
    
def today_active_doctors_count():
    return Availability.objects.filter(
        is_available=True,
        is_active=True,
        date=timezone.localdate()
    ).values('doctor').distinct().count()


def today_doctor_available_slots():
    today = timezone.localdate()
    return Availability.objects.filter(
        date=today,
        is_available=True,
        is_active=True
    ).count()
    
    
from django.db import transaction
from django.core.exceptions import ValidationError


@transaction.atomic
def create_availability(*, doctor, date, start_time, end_time):
    """
    Create doctor availability slot.
    Raises ValidationError if overlapping slot exists.
    """

    overlap_exists = Availability.objects.filter(
        doctor=doctor,
        date=date,
        start_time__lt=end_time,
        end_time__gt=start_time,
        is_available=True
    ).exists()

    if overlap_exists:
        raise ValidationError(
            "Availability overlaps with an existing slot."
        )

    return Availability.objects.create(
        doctor=doctor,
        date=date,
        start_time=start_time,
        end_time=end_time
    )
    

def get_current_week_range():
    today = timezone.localdate()  # timezone-safe
    # print(today)
    start_of_week = today - timedelta(days=today.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)          # Sunday
    return start_of_week, end_of_week