# apps/doctors/services.py
from apps.doctors.models import doctorprofile_model

def doctor_list(active_only=True):
    qs = doctorprofile_model.objects.all()
    if active_only:
        qs = qs.filter(is_active=True)
    return qs
