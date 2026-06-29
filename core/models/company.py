from django.db import models
from .city import City


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    city_name = models.ForeignKey(City, on_delete=models.CASCADE, related_name="companies")


    def __str__(self):
        return self.company_name