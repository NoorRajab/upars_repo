from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from .models import PointTransaction, UserProfile

@receiver(post_save, sender=PointTransaction)
def update_tier_and_points(sender, instance, **kwargs):
    if instance.verified:
        profile = instance.user.profile
        total = PointTransaction.objects.filter(
            user=instance.user, verified=True
        ).aggregate(Sum('points'))['points__sum'] or 0
        
        profile.total_points = total
        
        
        if total >= 3001: profile.tier = 'Platinum'
        elif total >= 2001: profile.tier = 'Gold'
        elif total >= 1001: profile.tier = 'Silver'
        else: profile.tier = 'Bronze'
        
        profile.save()