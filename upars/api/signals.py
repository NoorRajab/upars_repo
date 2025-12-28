from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PointTransaction, UserProfile

@receiver(post_save, sender=PointTransaction)
def update_tier_and_points(sender, instance, **kwargs):
    if instance.is_verified:
        profile = instance.user
        
        total = sum(t.points_awarded for t in PointTransaction.objects.filter(user=profile, is_verified=True))
        profile.total_points = total
        
        
        if total >= 3001: profile.tier = 'Platinum'
        elif total >= 2001: profile.tier = 'Gold'
        elif total >= 1001: profile.tier = 'Silver'
        else: profile.tier = 'Bronze'
        
        profile.save()