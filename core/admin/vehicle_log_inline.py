
from django.contrib import admin
from core.models import VehicleLog


class VehicleLogInline(admin.StackedInline):
    model = VehicleLog
    exclude = ("vehicle", )
    extra = 1


    def has_change_permission(self, request, obj = None):
        return False
