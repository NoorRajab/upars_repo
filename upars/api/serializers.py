from rest_framework import serializers
from .models import UserProfile, ActivityCategory, PointTransaction, RewardItem

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class PointTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointTransaction
        fields = '__all__'

class RewardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardItem
        fields = '__all__'