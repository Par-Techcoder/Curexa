from rest_framework import serializers
from apps.docbook.models import Appointment
from apps.docbook.models import Availability


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'appointment_type',
            'availability',
            'patient',
            'doctor',
            'notes',
        )

    def validate(self, attrs):
        availability: Availability = attrs['availability']
        doctor = attrs['doctor']

        # Availability must be free
        if not availability.is_available:
            raise serializers.ValidationError(
                {"availability": "This slot is already booked."}
            )

        # Availability must belong to the same doctor
        if availability.doctor_id != doctor.id:
            raise serializers.ValidationError(
                {"doctor": "Doctor does not match availability slot."}
            )

        return attrs

    def create(self, validated_data):
        availability = validated_data['availability']

        appointment = Appointment.objects.create(**validated_data)

        # Lock the slot
        availability.is_available = False
        availability.save(update_fields=['is_available'])

        return appointment

class AppointmentReadSerializer(serializers.ModelSerializer):
    date = serializers.DateField(source='availability.date', read_only=True)
    start_time = serializers.TimeField(source='availability.start_time', read_only=True)
    end_time = serializers.TimeField(source='availability.end_time', read_only=True)

    class Meta:
        model = Appointment
        fields = (
            'id',
            'appointment_type',
            'appointment_status',
            'patient',
            'doctor',
            'date',
            'start_time',
            'end_time',
            'notes',
            'created_at',
        )
