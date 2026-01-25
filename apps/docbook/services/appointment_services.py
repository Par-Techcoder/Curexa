from apps.docbook.models.appointment_model import Appointment
from apps.core.constants.default_values import AppointmentStatus, AppointmentType, Gender
from django.utils import timezone
from itertools import groupby
from operator import itemgetter

def active_appointments_count(doctor):
    return Appointment.objects.filter(
                doctor=doctor,
                appointment_status=AppointmentStatus.SCHEDULED.value,
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
        availability__is_active=True,
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
    

def full_name(first, middle, last):
    """Return a full name display name like 'John D. Doe'."""
    if middle:
        return f"{first} {middle[0]}. {last}"
    return f"{first} {last}"


def enum_name(enum_cls, value, default=None):
    """Get enum name from value, or default if not found."""
    if value in enum_cls._value2member_map_:
        return enum_cls(value).name
    return default


def age_from_dob(dob, on_date=None):
    """Calculate age from date of birth."""
    if not dob:
        return None   # or 0, or "", based on API needs

    if on_date is None:
        on_date = timezone.now().date()

    years = on_date.year - dob.year
    if (on_date.month, on_date.day) < (dob.month, dob.day):
        years -= 1
    return years


def _base_doctor_appointment_qs(date=None, start_date=None, end_date=None):
    # Base queryset
    qs = Appointment.objects.filter(is_active=True).values(
        # Doctor
        'doctor__id',
        'doctor__doctor__first_name',
        'doctor__doctor__middle_name',
        'doctor__doctor__last_name',
        'doctor__profile_picture',
        'doctor__specialization__department__name',

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

    # Apply date filters
    if date:
        qs = qs.filter(availability__date=date, availability__is_active=True)
    elif start_date and end_date:
        qs = qs.filter(availability__is_active=True, availability__date__range=(start_date, end_date))

    # Convert to list for Python-level processing
    appointments = list(qs.order_by('availability__date', 'availability__start_time'))

    for a in appointments:
        # Doctor
        a['doctor_id'] = a.pop('doctor__id')        
        a['doctor_name'] = full_name(
            a.pop('doctor__doctor__first_name', ''),
            a.pop('doctor__doctor__middle_name', ''),
            a.pop('doctor__doctor__last_name', '')
        )
        a['doctor_profile_picture'] = a.pop('doctor__doctor__profile_picture', None)
        a['doctor_department'] = a.pop('doctor__specialization__department__name', None)
        
        # Patient
        a['patient_id'] = a.pop('patient__id'),
        a['patient_name'] = full_name(
            a.pop('patient__patient__first_name', ''),
            a.pop('patient__patient__middle_name', ''),
            a.pop('patient__patient__last_name', '')
        )
        a['patient_email'] = a.pop('patient__patient__email', '')
        a['chronic'] = a.pop('patient__chronic_conditions', None)
        a['patient_age'] = age_from_dob(
            a.pop('patient__dob', None)
        )        
        a['patient_gender'] = enum_name(Gender, a.pop('patient__gender', '') )
        a['patient_mobile'] = a.pop('patient__phone_number', '')
        a['patient_allergies'] = a.pop('patient__allergies', None)
        
        a['appt_type'] = a.pop('appointment_type')
        a['appt_status'] = a.pop('appointment_status')   
        a['appt_notes'] = a.pop('notes')
        
        a['date'] = a.pop('availability__date')
        a['start_time'] = a.pop('availability__start_time')
        a['end_time'] = a.pop('availability__end_time')

    # Sort first by doctor, then by start time
    appointments.sort(key=itemgetter('doctor_id', 'start_time'))

    # Group by doctor ID
    grouped = {}
    for doctor_id, appts in groupby(appointments, key=itemgetter('doctor_id')):
        appts = list(appts)
        grouped[doctor_id] = {
            'doctor_name': appts[0]['doctor_name'],
            'appointments': appts,
        }

    return grouped


def doctors_appointments_today():
    return _base_doctor_appointment_qs(date=timezone.localdate())

def doctors_appointments_by_date(date):
    return _base_doctor_appointment_qs(date=date)

def doctors_appointments_in_current_week(start_date, end_date):
    return _base_doctor_appointment_qs(start_date=start_date, end_date=end_date)
    

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

