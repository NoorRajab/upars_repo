
from django.db import models
from django.contrib.auth.models import User

# Define roles as constants
ROLE_CHOICES = [
    ('Student', 'Student'),
    ('Staff', 'Staff'),
    ('Admin', 'Admin'),
]

class UserProfile(models.Model):
    """Extends the default User model with gamification and role data."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Role for RBAC (Student/Staff/Admin)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Student') 
    
    department = models.CharField(max_length=100, blank=True, null=True)
    total_points = models.IntegerField(default=0)
    enrollment_number = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class ActivityCategory(models.Model):
    """Defines types of achievements that can be rewarded."""
    name = models.CharField(max_length=100, unique=True)
    base_points = models.IntegerField(default=10) # Base points for the activity

    class Meta:
        verbose_name_plural = "Activity Categories"

    def __str__(self):
        return self.name

class PointTransaction(models.Model):
    """Audit log for all point movements."""
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='transactions')
    awarded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='awards_given')
    category = models.ForeignKey(ActivityCategory, on_delete=models.SET_NULL, null=True)
    points_amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.student.user.username}: {self.points_amount} points via {self.category.name}"