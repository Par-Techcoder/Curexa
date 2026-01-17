from apps.doctors.models.doctorprofile_model import DoctorProfile
from apps.docbook.models.appoinment_model import Appointment
from apps.core.constants.default_values import AppointmentStatus
from django.utils import timezone

def doctor_list():
    qs = DoctorProfile.objects.select_related(
        'doctor', 'specialization'
    )

    today = timezone.now().date()
    result = []

    for obj in qs:
        active_appointments_count = Appointment.objects.filter(
            doctor=obj,
            appointment_status=AppointmentStatus.PENDING.value,
            appointment_date=today
        ).count()

        todays_appointments_count = Appointment.objects.filter(
            doctor=obj,
            appointment_date=today
        ).exclude(
            appointment_status=AppointmentStatus.CANCELLED.value
        ).count()

        data = {
            "doctor_id": obj.doctor.id,
            "doctor_name": obj.doctor.get_full_name(),
            "contact_number": obj.contact_number,
            "profile_picture": obj.profile_picture.url if obj.profile_picture else None,
            "is_active": obj.doctor.is_active,
            "active_appointments_count": active_appointments_count,
            "todays_appointments_count": todays_appointments_count,
        }
                
        result.append(data)

    return result



def doctor_add(name, specialization, email, phone):
    DoctorProfile.objects.create(
        name=name,
        specialization=specialization,
        email=email,
        phone=phone,
    )
    
    