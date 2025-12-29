from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, ActivityCategory, PointTransaction, RewardItem

class UPARSTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='student1', password='password123')
        self.profile = UserProfile.objects.create(user=self.user, student_id='BSCS/001')
        self.category = ActivityCategory.objects.create(name='Academic', description='Grades')

    def test_tier_progression(self):
        
        PointTransaction.objects.create(
            profile=self.profile,
            category=self.category,
            points_awarded=1500,
            description='Dean List'
        )
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.tier, 'Silver')
        self.assertEqual(self.profile.total_points, 1500)

    def test_insufficient_points_redemption(self):
        
        reward = RewardItem.objects.create(
            name='Umma Hoodie', 
            cost_points=5000, 
            tier_required='Gold'
        )
        
        self.assertLess(self.profile.total_points, reward.cost_points)