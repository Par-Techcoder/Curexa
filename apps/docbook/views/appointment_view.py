from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.docbook.serializers.appointment_serializer import AppointmentCreateSerializer


class AppointmentBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AppointmentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        appointment = serializer.save()

        return Response(
            {
                "id": appointment.id,
                "message": "Appointment booked successfully"
            },
            status=status.HTTP_201_CREATED
        )
