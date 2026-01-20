# apps/core/permissions.py
from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    """
    Generic role-based permission for Django REST Framework (DRF).

    How to use:
    1. In your APIView (CBV) or function-based API (FBV), set the `allowed_roles` attribute
       to a list of roles allowed to access that endpoint.
       Example: RolePermission.allowed_roles = [Role.ADMIN.value]

    2. Add RolePermission to `permission_classes` along with IsAuthenticated:
       permission_classes = [IsAuthenticated, RolePermission]

    3. Multiple roles can be allowed:
       RolePermission.allowed_roles = [Role.ADMIN.value, Role.DOCTOR.value]

    4. If the user is not authenticated or role does not match, DRF automatically
       returns a 403 Forbidden response with the `message`.

    Example usage:

    CBV (Class-Based View):
        class AdminDashboardAPI(APIView):
            permission_classes = [IsAuthenticated, RolePermission]
            RolePermission.allowed_roles = [Role.ADMIN.value]

            def get(self, request):
                return Response({"email": request.user.email})

    FBV (Function-Based View):
        @api_view(['GET'])
        @permission_classes([IsAuthenticated, RolePermission])
        def doctor_dashboard(request):
            RolePermission.allowed_roles = [Role.DOCTOR.value]
            return Response({"message": "Welcome Doctor"})
    """

    allowed_roles = []  # Override this in your view
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        # Check user exists and is authenticated
        if not (request.user and request.user.is_authenticated):
            return False

        # Check if user's role is in the allowed_roles list
        return request.user.role in self.allowed_roles
