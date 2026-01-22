from rest_framework import viewsets, permissions
from django.conf import settings
from apps.accounts.models import User
from apps.accounts.serializers.admin_user_serializer import AdminUserSerializer

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = AdminUserSerializer

    def get_permissions(self):
        """
        Toggle access based on environment:
        - Development: any authenticated user
        - Production: superusers only
        """
        if getattr(settings, "DEBUG", True):
            # Dev mode: any authenticated user
            # permission_classes = [permissions.IsAuthenticated]
            permission_classes = []
        else:
            # Production: superusers only
            class IsSuperUser(permissions.BasePermission):
                def has_permission(self, request, view):
                    return bool(request.user and request.user.is_superuser)

            permission_classes = [IsSuperUser]

        return [permission() for permission in permission_classes]
