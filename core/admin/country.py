from django.contrib import admin
from ..models import Country


class CountryInline(admin.StackedInline):
    model = Country
    max_num = 1