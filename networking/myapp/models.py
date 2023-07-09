from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    referral_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals_made')
    referred_email = models.EmailField()
    referred_name = models.CharField(max_length=255)
    referral_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('referrer', 'referral_code')


class Commission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissions_earned')
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission_date = models.DateField(auto_now_add=True)