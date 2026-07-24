from django.contrib import admin
from ..models import Invoice


class InvoiceAdmin(admin.StackedInline):
    model = Invoice