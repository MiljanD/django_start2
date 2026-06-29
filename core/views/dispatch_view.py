from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import Shipment


class DispatchView(UserPassesTestMixin, ListView):
    model = Shipment
    template_name = "dispatch.html"
    context_object_name = "data"


    def get_queryset(self, queryset = None):
        return Shipment.objects.filter(dispatcher=self.request.user)


    def test_func(self):
        return self.request.user.profile.user_type in ["admin", "dispatcher"]