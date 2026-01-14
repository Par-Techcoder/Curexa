from rest_framework import serializers
from apps.doctors.models import doctorprofile_model 

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctorprofile_model
        fields = ['id', 'name', 'specialization', 'is_active']
