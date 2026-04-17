
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from core.models.profile import Profile
from core.models.vehicle_log import VehicleLog
from core.forms.vehicle_log_form import VehicleLogForm
from django.urls import reverse_lazy
from django.utils import timezone


class ProfileView(TemplateView):
    template_name = "profile.html"


    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = timezone.now().date()

        has_log_today = VehicleLog.objects.filter(user=self.request.user, return_time__date=current_date).exists()

        form = None
        if not has_log_today:
            form = VehicleLogForm()

        context.update({"form": form, "show_form": not has_log_today})

        return context


    def post(self, request, *args, **kwargs):
        form = VehicleLogForm(request.POST)
        if form.is_valid():
            vehicle_log = form.save(commit=False)
            vehicle_log.user = self.request.user
            vehicle_log.save()
            return HttpResponseRedirect(reverse_lazy("profile"))

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)

