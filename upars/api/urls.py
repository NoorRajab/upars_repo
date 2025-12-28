from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeaderboardViewSet, student_dashboard

router = DefaultRouter()
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('dashboard/', student_dashboard, name='student_dashboard'), 
    path('v1/', include(router.urls)), 
]