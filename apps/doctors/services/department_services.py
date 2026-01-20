from apps.doctors.models.department_model import Department

def get_all_departments():
    return Department.objects.filter(is_active=True)