
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    USER_TYPE_CHOICES = (
        ("admin", "Administrator"),
        ("dispatcher", "Dispatcher"),
        ("driver", "Driver")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)