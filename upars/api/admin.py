from django.contrib import admin
from .models import UserProfile, ActivityCategory, PointTransaction, RewardItem, Redemption

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'total_points', 'tier')
    list_filter = ('tier',)

@admin.register(PointTransaction)
class PointTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'category', 'verified')
    list_editable = ('verified',) 

admin.site.register(ActivityCategory)
admin.site.register(RewardItem)
admin.site.register(Redemption)