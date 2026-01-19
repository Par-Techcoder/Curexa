from rest_framework import serializers
from accounts.models import User, Role

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

        # Create staff user
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=role,
            is_staff=True
        )

        # Optional: Add audit logging here
        request_user = self.context['request'].user
        print(f"[Audit] {request_user.email} created admin {user.email} with role {role}")

        return user
