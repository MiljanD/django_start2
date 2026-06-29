
from .admin_site import admin_site
from django.contrib.auth.models import User
from core.models.vehicles import Vehicles
from core.models.vehicle_log import VehicleLog
from core.admin.custom_user_admin import CustomUserAdmin
from .country import *
from .city import *
from .company import *
from .shipment import *




# admin_site.unregister(User)
# admin_site.register(User, CustomUserAdmin)

admin_site.register(Vehicles)
admin_site.register(VehicleLog)
admin_site.register(Country)
admin_site.register(City)
admin_site.register(Company)
admin_site.register(Shipment)



