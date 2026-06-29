from django.contrib import admin
from ..models import Shipment


class ShipmentInline(admin.StackedInline):
    model = Shipment
    max_num = 1