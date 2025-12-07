
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, ActivityCategory, PointTransaction

class UserSerializer(serializers.ModelSerializer):
    """Basic serializer for the default User model."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for the UserProfile, including nested User details."""
    user = UserSerializer(read_only=True) # Nested read-only user details

    class Meta:
        model = UserProfile
        fields = [
            'id', 
            'user', 
            'role', 
            'department', 
            'total_points', 
            'enrollment_number'
        ]
        read_only_fields = ['total_points', 'role'] # Points and role set by system/admin

class ActivityCategorySerializer(serializers.ModelSerializer):
    """Serializer for ActivityCategory."""
    class Meta:
        model = ActivityCategory
        fields = ['id', 'name', 'base_points']