from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        allowed_roles = getattr(view, 'allowed_roles', None)

        if not allowed_roles:
            return False

        return request.user.role in allowed_roles
