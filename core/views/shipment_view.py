from django.views.generic import TemplateView
from ..forms import ShipmentForm
from django.shortcuts import redirect
from django.db.models import Model



class ShipmentView(TemplateView):
    template_name = "shipment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ShipmentForm()
        return context

    def post(self, request, *args, **kwargs):
        shipment = self.request.session.get("shipment", {})
        form = ShipmentForm(request.POST)

        if form.is_valid():
            shipment_data = {}
            for field in form.Meta.fields:
                field_value = form.cleaned_data[field]
                if isinstance(field_value, Model):
                    shipment_data[f"{field}_id"] = field_value.id
                else:
                    shipment_data[field] = field_value

            self.request.session["shipment"] = shipment_data
            self.request.session.modified = True

            return redirect("submit_shipment")
        return redirect("generate_shipment")