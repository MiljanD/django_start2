
from django.db import models
from django.contrib.auth.models import User
from .vehicles import Vehicles
from django.utils import timezone


class VehicleLog(models.Model):
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField()
    return_time = models.DateTimeField(default=timezone.now)