from apps.doctors.models.doctorprofile_model import DoctorProfile

def doctor_list(active_only=True):
    qs = DoctorProfile.objects.all()        
    return qs
