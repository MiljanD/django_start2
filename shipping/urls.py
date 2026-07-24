"""
URL configuration for shipping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from core.views import (ProfileView, DispatchView,
                        ShipmentUpdateView, ShipmentView,
                        ShipmentPriceCalculationView, GenerateInvoiceView)
from core.admin import admin_site
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin_site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/'), name='login_page'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dispatch/', DispatchView.as_view(), name='dispatch'),
    path('shipment/<int:pk>/edit', ShipmentUpdateView.as_view(), name="shipment_edit"),
    path('shipment/generate/', ShipmentView.as_view(), name='generate_shipment'),
    path('shipment/submit/', ShipmentPriceCalculationView.as_view(), name='submit_shipment'),
    path('shipment/<int:pk>/generate-invoice/', GenerateInvoiceView.as_view(), name='generate-invoice')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
