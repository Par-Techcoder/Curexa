from apps.doctors.models.doctorprofile_model import DoctorProfile
from apps.docbook.services import appointment_services
from apps.docbook.services import availability_services

from django.db.models import Exists, OuterRef
from apps.docbook.models.availability_model import Availability
from django.utils.timezone import now



def doctor_queryset():
    return DoctorProfile.objects.select_related(
        "doctor", "specialization"
    ).prefetch_related(
        "fk_qualifications_doctor_profile_doctor_id"
    ).annotate(
        is_available_today=Exists(
            Availability.objects.filter(
                doctor=OuterRef("pk"),
                date=now().date(),
                is_active=True
            )
        )
    )


def doctor_list_data(qs):
    result = []

    for obj in qs:
        result.append({
            "id": obj.doctor.id,
            "name": obj.doctor.get_full_name(),
            "email": obj.doctor.email,
            "specialization": obj.specialization.name if obj.specialization else "",
            "contact_number": obj.contact_number,
            "profile_picture": obj.profile_picture.url if obj.profile_picture else "",
            # "available": obj.is_available,  # annotate later if needed
        })

    return result

def doctor_add(dr_user, license_number, license_expiry_date, profile_picture,
               consultation_fee, experience_years, bio, dob, clinic_address, specialization=None, city=None, pin_code=None, contact_number=None):
    return DoctorProfile.objects.create(
        doctor=dr_user,
        license_number=license_number,
        license_expiry=license_expiry_date,        
        consultation_fee=consultation_fee,     
        specialization=specialization,
        experience_years=experience_years,
        bio=bio,
        dob=dob,
        clinic_address=clinic_address,
        city=city,
        pin_code=pin_code,
        contact_number=contact_number,
        profile_picture=profile_picture
    )

    
def total_doctors_count():
    return DoctorProfile.objects.count()

def specialized_doctors_count():
    return DoctorProfile.objects.filter(specialization__isnull=False).count()

def get_all_doctors():
    return DoctorProfile.objects.values(
        'id',        
        'doctor__first_name',
        'doctor__middle_name',
        'doctor__last_name',
        'profile_picture',
        'specialization__name'
    )
