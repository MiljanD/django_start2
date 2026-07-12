
from django.views.generic import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import Shipment
from ..forms import ShipmentUpdateForm
from django.urls import reverse_lazy



class ShipmentUpdateView(UserPassesTestMixin,UpdateView):
    model = Shipment
    form_class = ShipmentUpdateForm
    template_name = "shipment_edit.html"
    success_url = reverse_lazy("dispatch")


    def test_func(self):
        return self.request.user.profile.user_type in ["admin", "dispatcher"]

    def get_queryset(self):
        return Shipment.objects.filter(dispatcher=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["history"] = self.object.history.all()
        return context
