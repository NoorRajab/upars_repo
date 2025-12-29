from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/admin/login/')
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    transactions = PointTransaction.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'api/dashboard.html', {'profile': profile, 'transactions': transactions})

def leaderboard_view(request):
    students = UserProfile.objects.order_by('-total_points')[:10]
    return render(request, 'api/leaderboard.html', {'students': students})

def rewards_catalog(request):
    rewards = RewardItem.objects.all()
    return render(request, 'api/rewards.html', {'rewards': rewards})


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class PointTransactionViewSet(viewsets.ModelViewSet):
    queryset = PointTransaction.objects.all()
    serializer_class = TransactionSerializer