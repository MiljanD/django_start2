from core.admin.profile_inline import ProfileInline
from core.admin.vehicles_inline import VehiclesInline
from core.admin.vehicle_log_inline import VehicleLogInline
from django.contrib.auth.admin import UserAdmin
from core.models.vehicle_log import VehicleLog
from core.models.vehicles import Vehicles



class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, VehiclesInline, VehicleLogInline, )


    def save_formset(self, request, form, formset, change):

        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, VehicleLog):
                vehicle = Vehicles.objects.filter(user=form.instance).first()

                if vehicle:
                    instance.vehicle = vehicle

            instance.save()

        formset.save_m2m()
