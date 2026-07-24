from django.contrib import admin
from ..models import Shipment
from django.db.models import Model
from django.shortcuts import redirect



class ShipmentAdmin(admin.ModelAdmin):
    REDIRECT = False
    fields = ["title", "description", "company",
              "pickup_location", "delivery_location", "status",
              "dispatcher", "driver", "vehicle", "notes"]

    def save_model(self, request, obj, form, change):
        if not change:
            shipment_data = {}
            for field in form.cleaned_data:
                field_value = form.cleaned_data[field]
                if isinstance(field_value, Model):
                    shipment_data[f"{field}_id"] = field_value.id
                else:
                    shipment_data[field] = field_value

            request.session["shipment"] = shipment_data
            request.session["from_admin"] = True
            request.session.modified = True

            self.REDIRECT = True
        else:
            super().save_model(request, obj, form, change)


    def response_add(self, request, obj, post_url_continue = ...):

        if getattr(self, "REDIRECT", True):
            self.REDIRECT = False
            return redirect("submit_shipment")

        return super().response_add(request, obj, post_url_continue)





