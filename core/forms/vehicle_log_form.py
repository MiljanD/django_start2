
from django import forms
from core.models.vehicle_log import VehicleLog

class VehicleLogForm(forms.ModelForm):
    class Meta:
        model = VehicleLog
        fields = ["mileage"]