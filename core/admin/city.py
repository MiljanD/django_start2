from django.contrib import admin
from ..models import City


class CityInline(admin.StackedInline):
    model = City
    max_num = 1