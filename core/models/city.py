from django.db import models
from .country import Country

class City(models.Model):
    city_name = models.CharField(max_length=64, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")


    def __str__(self):
        return f"{self.city_name}, {self.country.country_name}"
