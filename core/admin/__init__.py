from django.contrib import admin
from django.contrib.auth.models import User
from core.models.vehicles import Vehicles
from core.models.vehicle_log import VehicleLog
from core.admin.custom_user_admin import CustomUserAdmin




admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Vehicles)
admin.site.register(VehicleLog)



