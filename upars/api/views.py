
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, ActivityCategory
from .serializers import UserProfileSerializer, ActivityCategorySerializer
from .permissions import IsStaffOrAdmin, IsOwnerOrStaffOrAdmin
from django.shortcuts import get_object_or_404

class UserProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin):
    """
    Handles user profiles. Allows Students to view/patch their own profile.
    Staff/Admin can view all, but update is limited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaffOrAdmin] # Uses the custom permission

    def get_queryset(self):
        """
        Students can only see their own profile. Staff/Admin can see all.
        """
        user = self.request.user
        if not user.is_authenticated:
            return UserProfile.objects.none()

        try:
            profile = user.profile
        except UserProfile.DoesNotExist:
            return UserProfile.objects.none()

        # Staff or Admin can list all profiles
        if profile.role in ['Staff', 'Admin']:
            return UserProfile.objects.all()
        
        # Students can only see their own profile
        return UserProfile.objects.filter(user=user)

class ActivityCategoryViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Activity Categories. Restricted to Staff/Admin.
    """
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin] # Restricted to Staff/Admin