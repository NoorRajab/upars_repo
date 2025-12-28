from rest_framework import viewsets
from django.shortcuts import render
from .models import UserProfile, PointTransaction, RewardItem
from .serializers import UserProfileSerializer


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all().order_by('-total_points')[:10]
    serializer_class = UserProfileSerializer


def student_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    transactions = PointTransaction.objects.filter(user=profile)
    rewards = RewardItem.objects.filter(required_points__lte=profile.total_points)
    return render(request, 'api/dashboard.html', {
        'profile': profile,
        'transactions': transactions,
        'rewards': rewards
    })