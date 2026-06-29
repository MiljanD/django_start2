
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):

    def has_permission(self, request):
        return (
            request.user.is_authenticated and
            getattr(request.user.profile, "user_type", None) == "admin"
        )


admin_site = MyAdminSite(name='myadmin')
