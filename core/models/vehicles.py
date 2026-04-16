
from django.db import models
from django.contrib.auth.models import User


class Vehicles(models.Model):

    VEHICLE_TYPE_CHOICES = (
        ("truck", "Truck"),
        ("van", "Van"),
        ("car", "Car")
    )

    STATUS_CHOICES = (
        ("available", "Available"),
        ("in_use", "In Use"),
        ("maintenance", "Maintenance"),
        ("inactive", "Inactive")
    )


    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    plate_number = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    workhours = models.PositiveIntegerField(default=0)
    capacity = models.FloatField(help_text="Max load in kg")


    def __str__(self):
        return f"{self.plate_number} ({self.vehicle_type})"

