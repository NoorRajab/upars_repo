from django.db import models
from django.contrib.auth.models import User

class ActivityCategory(models.Model):
    name = models.CharField(max_length=100) 
    weighting_constant = models.IntegerField(default=25)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    total_points = models.FloatField(default=0.0)
    tier = models.CharField(max_length=20, default='Bronze') 

class PointTransaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    points_awarded = models.FloatField()
    is_verified = models.BooleanField(default=False) 
    timestamp = models.DateTimeField(auto_now_add=True)

class RewardItem(models.Model):
    name = models.CharField(max_length=100)
    required_points = models.IntegerField()
    tier_required = models.CharField(max_length=20)
    stock = models.IntegerField(default=10)