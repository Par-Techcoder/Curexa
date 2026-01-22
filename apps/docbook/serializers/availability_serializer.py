from rest_framework import serializers
from apps.docbook.models import Availability

class AvailabilityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = [
            'doctor',
            'date',
            'start_time',
            'end_time',
        ]

    def validate(self, attrs):
        if attrs['start_time'] >= attrs['end_time']:
            raise serializers.ValidationError(
                "Start time must be before end time."
            )
        return attrs
