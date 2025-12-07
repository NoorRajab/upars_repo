# api_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api.views import UserProfileViewSet, ActivityCategoryViewSet

# Create a router and register our ViewSets
router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='profile')
router.register(r'categories', ActivityCategoryViewSet, basename='category')
# Transactions, Rewards, and Redemption ViewSets will be added later (Week 2/3)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Token Authentication endpoint
    path('api/auth-token/', obtain_auth_token, name='auth_token'),
    
    # API endpoints using the router
    path('api/', include(router.urls)),
]