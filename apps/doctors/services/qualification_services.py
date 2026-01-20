from apps.doctors.models.qualification_model import Qualification

def add_qualification(doctor, degree, institution, completion_year):
    return Qualification.objects.create(
        doctor=doctor,
        degree=degree,
        institution=institution,
        completion_year=completion_year
    )