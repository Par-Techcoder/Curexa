from rest_framework.permissions import IsAuthenticated
from apps.core.utilities.permissions import RolePermission
from apps.core.constants.default_values import Role
from apps.docbook.serializers.availability_serializer import AvailabilityCreateSerializer
from apps.docbook.services import availability_services
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AvailabilityCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, RolePermission]
    allowed_roles = [Role.ADMIN.value, Role.DOCTOR.value]

    def post(self, request):
        serializer = AvailabilityCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        availability = availability_services.create_availability(
            doctor=serializer.validated_data['doctor'],
            date=serializer.validated_data['date'],
            start_time=serializer.validated_data['start_time'],
            end_time=serializer.validated_data['end_time'],
        )

        return Response(
            {
                "id": availability.id,
                "message": "Availability created successfully"
            },
            status=status.HTTP_201_CREATED
        )
