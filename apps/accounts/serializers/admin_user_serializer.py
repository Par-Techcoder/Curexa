from rest_framework import serializers
from apps.accounts.models import User
from apps.core.constants.default_values import Role
from apps.accounts.services import user_services

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data['role']

        # Prevent creating superusers via API
        if role == Role.SUPERUSER.value:
            raise serializers.ValidationError("Cannot create superuser via API.")

        email = validated_data['email']
        password = validated_data['password']

        # Create staff user
        user = User.objects.create_user( 
            email=email,
            password=password,
            role=role
        )
        if role == Role.PATIENT.value:
            user_services.ensure_user_profile(user)
        elif role == Role.DOCTOR.value:
            user_services.ensure_user_profile(user)

        # Optional: audit logging
        request_user = self.context['request'].user
        print(f"[Audit] {request_user.email} created admin {user.email} with role {role}")

        return user
