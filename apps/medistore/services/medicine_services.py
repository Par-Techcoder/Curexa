from apps.medistore.models.medicines_model import Medicine

def get_all_medicines():
    return Medicine.objects.all()