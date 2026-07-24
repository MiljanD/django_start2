
from django import forms
from ..models import Shipment


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["title", "description", "company",
                  "pickup_location", "delivery_location", "status",
                  "dispatcher", "driver", "vehicle", "notes"]

