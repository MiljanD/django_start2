
from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal


class Profile(models.Model):

    USER_TYPE_CHOICES = (
        ("admin", "Administrator"),
        ("dispatcher", "Dispatcher"),
        ("driver", "Driver")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("1.50"))
