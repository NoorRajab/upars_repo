from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.UserProfileViewSet)
router.register(r'transactions', views.PointTransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.dashboard, name='dashboard'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('rewards/', views.rewards_catalog, name='rewards'),
]