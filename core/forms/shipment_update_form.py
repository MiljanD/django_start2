from django import forms
from ..models import Shipment


class ShipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["status", "driver", "vehicle"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        driver_qs = self.fields["driver"].queryset.exclude(
            assigned_shipments__status=Shipment.Status.ENROUTE
        )

        if self.instance and self.instance.pk and self.instance.driver_id:
            driver_qs = driver_qs | self.fields["driver"].queryset.filter(
                pk=self.instance.driver_id
            )

        self.fields["driver"].queryset = driver_qs.distinct()

        vehicle_qs = self.fields["vehicle"].queryset.exclude(
            shipment__status=Shipment.Status.ENROUTE
        )

        if self.instance and self.instance.pk and self.instance.vehicle_id:
            vehicle_qs = vehicle_qs | self.fields["vehicle"].queryset.filter(
                pk=self.instance.vehicle_id
            )

        self.fields["vehicle"].queryset = vehicle_qs.distinct()


