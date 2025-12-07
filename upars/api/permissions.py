
from rest_framework import permissions

class IsStaffOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow only 'Staff' or 'Admin' users access.
    Checks the role field on the UserProfile.
    """
    def has_permission(self, request, view):
        # Allow read access for safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check the role in the UserProfile
        try:
            profile = request.user.profile
            return profile.role in ['Staff', 'Admin']
        except UserProfile.DoesNotExist:
            return False

class IsOwnerOrStaffOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow an object's owner, Staff, or Admin users access.
    Used for profile viewing/editing.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read permissions to anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is the owner
        if request.user == obj.user:
            return True

        # Check for Staff or Admin role for CUD operations
        try:
            profile = request.user.profile
            return profile.role in ['Staff', 'Admin']
        except UserProfile.DoesNotExist:
            return False