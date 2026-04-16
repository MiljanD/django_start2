
from django.contrib import admin
from core.models import VehicleLog


class VehicleLogInline(admin.StackedInline):
    model = VehicleLog
    exclude = ("vehicle", )
    extra = 1
