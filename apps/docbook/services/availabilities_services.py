from apps.docbook.models.availability_model import Availability
from django.utils import timezone

def check_doctor_availability(doctor, date, time_slot):
    return Availability.objects.filter(
        doctor=doctor,
        date=date,
        time_slot=time_slot,
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
        date=timezone.localdate()
    ).values('doctor').distinct().count()


def today_doctor_available_slots():
    today = timezone.localdate()
    return Availability.objects.filter(
        date=today,    
        is_available=True
    )
    
    