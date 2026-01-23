from apps.docbook.models.appointment_model import Appointment
from apps.core.constants.default_values import AppointmentStatus, AppointmentType
from django.utils import timezone

def active_appointments_count(doctor):
    return Appointment.objects.filter(
                doctor=doctor,
                appointment_status=AppointmentStatus.Scheduled.value,
                availability__is_available=True,
                availability__date=timezone.now().date(),
            ).count()

def todays_appointments_count_by_doctor(doctor):
    return Appointment.objects.filter(
        doctor=doctor,
        availability__is_available=True,
        availability__date=timezone.now().date(),
        is_active=True
    ).exclude(
        appointment_status=AppointmentStatus.CANCELLED.value
    ).count()
    
def todays_appointments_count_for_all_doctors():
    return Appointment.objects.filter(
        availability__is_available=True,
        availability__date=timezone.now().date(),
        is_active=True
    ).exclude(
        appointment_status=AppointmentStatus.CANCELLED.value
    ).count()

def todays_emergency_appointments_count():
    return Appointment.objects.filter(
        appointment_type=AppointmentType.EMERGENCY.value,
        is_active=True,
        availability__date=timezone.now().date()
    ).count()
    

def _base_doctor_appointment_qs():
    return (
        Appointment.objects
        .filter(is_active=True)
        .select_related(
            'doctor__doctor',
            'patient__user',
            'availability'
        )
        .values(
            # Doctor
            'doctor__id',
            'doctor__doctor__first_name',
            'doctor__doctor__middle_name',
            'doctor__doctor__last_name',

            # Patient
            'patient__id',
            'patient__patient__first_name',
            'patient__patient__middle_name',
            'patient__patient__last_name',
            'patient__dob',
            'patient__gender',
            'patient__patient__email',
            'patient__phone_number',
            'patient__chronic_conditions',
            'patient__allergies',

            # Appointment
            'appointment_type',
            'appointment_status',
            'notes',

            # Availability
            'availability__date',
            'availability__start_time',
            'availability__end_time',
        )
        .order_by(
            'availability__date',
            'availability__start_time'
        )
    )


def doctors_appointments_today():
    today = timezone.now().date()
    return _base_doctor_appointment_qs().filter(
        availability__date=today
    )

def doctors_appointments_by_date(date):
    return _base_doctor_appointment_qs().filter(
        availability__date=date
    )


def doctors_appointments_in_current_week(start_date, end_date):
    return _base_doctor_appointment_qs().filter(
        availability__date__range=(start_date, end_date)
    )
    

def get_all_appointment_types_status():
    types = [
        {'name': t.name, 'value': t.value}
        for t in AppointmentType
    ]
    statuses = [
        {'name': s.name, 'value': s.value}
        for s in AppointmentStatus
    ]
    return {
        'types': types,
        'statuses': statuses
    }
