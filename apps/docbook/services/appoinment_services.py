from apps.docbook.models.appoinment_model import Appointment
from apps.core.constants.default_values import AppointmentStatus
from django.utils import timezone

def active_appointments_count(doctor):
    return Appointment.objects.filter(
                doctor=doctor,
                appointment_status=AppointmentStatus.PENDING.value,
                appointment_date=timezone.now().date()
            ).count()

def todays_appointments_count(doctor):
    return Appointment.objects.filter(
        doctor=doctor,
        appointment_date=timezone.now().date()
    ).exclude(
        appointment_status=AppointmentStatus.CANCELLED.value
    ).count()