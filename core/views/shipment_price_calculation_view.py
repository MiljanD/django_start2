from django.views.generic import FormView
from ..services import ShipmentService
from ..forms import PriceCalculationForm
from ..models import City
from django.shortcuts import redirect



class ShipmentPriceCalculationView(FormView):
    cities = []
    template_name = "shipment_price_calculation.html"
    form_class = PriceCalculationForm


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        shipment = self.request.session.get("shipment")
        from_city_data = City.objects.get(id=shipment["pickup_location_id"])
        to_city_data = City.objects.get(id=shipment["delivery_location_id"])

        self.cities = ShipmentService.collect_city_data(from_city_data, to_city_data)

        from_city_names = [f"{city["properties"]["name"]}, {city["properties"]["country"]}" for city in self.cities[0]]
        to_city_names = [f"{city["properties"]["name"]}, {city["properties"]["country"]}" for city in self.cities[1]]
        options = [from_city_names, to_city_names]
        kwargs["dropdown_options"] = options

        return kwargs


    def form_valid(self, form):
        shipment_data = self.request.session.get("shipment")
        city_from_idx = int(form.cleaned_data["city_from"])
        city_to_idx = int(form.cleaned_data["city_to"])

        origin_coords = ShipmentService.get_city_coords(self.cities[0], city_from_idx)
        destination_coords = ShipmentService.get_city_coords(self.cities[1], city_to_idx)
        distance = ShipmentService.calculate_distance(origin_coords, destination_coords)

        shipment_data["distance"] = distance
        shipment_data["price"] = distance * ShipmentService.price_per_km
        shipment_data["dispatcher_id"] = self.request.user.id


        ShipmentService.create_shipment(**shipment_data)

        from_admin = self.request.session.get("from_admin", False)
        del self.request.session["shipment"]
        if "from_admin" in self.request.session:
            del self.request.session["from_admin"]

        self.request.session.modified = True

        if from_admin:
            return redirect("admin:core_shipment_changelist")
        else:
            return redirect("dispatch")





