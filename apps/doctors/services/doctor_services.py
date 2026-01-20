from apps.doctors.models.doctorprofile_model import DoctorProfile
from apps.docbook.services import appoinment_services
from apps.docbook.services import availabilities_services

def doctor_list():
    qs = DoctorProfile.objects.select_related(
        'doctor', 'specialization'
    )
    
    result = []

    for obj in qs:
        
        active_appointments_count = appoinment_services.active_appointments_count(obj)
        todays_appointments_count = appoinment_services.todays_appointments_count(obj)
        today_availabilities = bool(availabilities_services.today_doctor_availabilities(obj))        
        
        data = {
            "id": obj.doctor.id,
            "name": obj.doctor.get_full_name(),
            "email": obj.doctor.email,
            "qualifications": list(
                obj.fk_qualifications_doctor_profile_doctor_id
                .filter(is_active=True)
                .values_list('degree', flat=True)
            ),
            "specialization": obj.specialization.name if obj.specialization else None,
            "contact_number": obj.contact_number,
            "profile_picture": obj.profile_picture.url if obj.profile_picture else None,
            "available": today_availabilities,
            "active_appointments_count": active_appointments_count,
            "todays_appointments_count": todays_appointments_count,
        }
                
        result.append(data)

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