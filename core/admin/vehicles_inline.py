
from django.contrib import admin
from core.models import Vehicles


class VehiclesInline(admin.StackedInline):
    model = Vehicles
    max_num = 1