
from django.views.generic import TemplateView
from core.models.profile import Profile
from core.models.vehicle_log import VehicleLog
from ..forms import VehicleLogForm
from django.utils import timezone
from django.shortcuts import redirect
from ..services import VehicleLogService


class ProfileView(TemplateView):
    template_name = "profile.html"


    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        state = VehicleLogService.get_state(self.request.user)

        if state["vehicle"] is None:
            context["has_vehicle"] = False
            return context

        context["already_logged"] = state["already_logged"]

        if not state["already_logged"]:
            context["form"] = VehicleLogForm()

        return context


    def post(self, request, *args, **kwargs):
        state = VehicleLogService.get_state(self.request.user)

        if state["vehicle"] is None or state["already_logged"]:
            return redirect("profile")

        form = VehicleLogForm(request.POST)

        if form.is_valid():
            VehicleLogService.create_log(
                user=self.request.user,
                mileage=form.cleaned_data["mileage"]
            )

        return redirect("profile")



