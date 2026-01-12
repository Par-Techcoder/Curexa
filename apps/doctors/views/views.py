from rest_framework import generics
from apps.doctors.serializers.doctor_serializer import DoctorSerializer
from apps.doctors.services import doctor_services

class DoctorListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        # Call service layer
        return doctor_services.doctor_list()
