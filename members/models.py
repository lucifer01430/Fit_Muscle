from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

class Membership(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('pro', 'Pro'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def days_left(self):
        return (self.end_date - date.today()).days

    def __str__(self):
        return f"{self.user.username} - {self.plan}"
