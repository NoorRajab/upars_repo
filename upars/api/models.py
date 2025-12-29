from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    student_id = models.CharField(max_length=20, unique=True)
    total_points = models.IntegerField(default=0)
    tier = models.CharField(max_length=20, default='Bronze')

    def __str__(self):
        return f"{self.user.username} ({self.student_id})"

class ActivityCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Activity Categories"

    def __str__(self):
        return self.name

class PointTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(ActivityCategory, on_delete=models.SET_NULL, null=True)
    points = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.points}"

class RewardItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    points_required = models.IntegerField()
    tier_required = models.CharField(max_length=20, default='Bronze')

    def __str__(self):
        return self.name

class Redemption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.ForeignKey(RewardItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)