from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class LoyaltyProgram(models.Model):
    TIER_CHOICES = [
        ('BRONZE', 'Bronze'),
        ('SILVER', 'Silver'),
        ('GOLD', 'Gold'),
        ('PLATINUM', 'Platinum'),
    ]
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    tier = models.CharField(max_length=50, choices=TIER_CHOICES, default='BRONZE')
    points = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.customer} - {self.membership_level} ({self.points} points)"