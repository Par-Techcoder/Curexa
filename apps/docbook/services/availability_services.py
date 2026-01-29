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

def get_current_month_range():
    today = timezone.localdate()

    # First day of current month
    start_of_month = today.replace(day=1)

    # First day of next month
    if today.month == 12:
        next_month = today.replace(year=today.year + 1, month=1, day=1)
    else:
        next_month = today.replace(month=today.month + 1, day=1)

    # Last day of current month
    end_of_month = next_month - timedelta(days=1)

    return start_of_month, end_of_month


@transaction.atomic
def toggle_slot_availability(availability_id):
    availability = Availability.objects.select_for_update().get(
        id=availability_id
    )

    availability.is_available = not availability.is_available
    availability.save(update_fields=["is_available"])

    return availability

@transaction.atomic
def toggle_doctor_leave(doctor, date):
    leave_row = Availability.objects.filter(
        doctor=doctor,
        date=date,
        start_time__isnull=True,
        is_leave=True
    ).first()

    # 🔴 If already on leave → remove leave
    if leave_row:
        leave_row.delete()
        return {
            "on_leave": False,
            "message": "Doctor is available for the day"
        }

    # 🟢 If not on leave → mark full-day leave
    Availability.objects.create(
        doctor=doctor,
        date=date,
        start_time=None,
        end_time=None,
        is_leave=True,
        is_available=False
    )

    return {
        "on_leave": True,
        "message": "Doctor marked on full-day leave"
    }


def is_doctor_on_leave(doctor, date):
    return Availability.objects.filter(
        doctor=doctor,
        date=date,
        is_leave=True
    ).exists()
