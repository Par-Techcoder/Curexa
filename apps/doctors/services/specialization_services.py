from apps.doctors.models.specialization_model import Specialization

def get_all_specializations():
    return Specialization.objects.filter(is_active=True)

def get_specialization_by_id(specialization_id):
    try:
        return Specialization.objects.get(id=specialization_id, is_active=True)
    except Specialization.DoesNotExist:
        return None