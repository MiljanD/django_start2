from django.db import models
from .shipment import Shipment
from simple_history.models import HistoricalRecords
from django.utils import timezone
from datetime import timedelta


class Invoice(models.Model):
    class Status(models.TextChoices):
        PAID = "paid", "Paid"
        UNPAID = "unpaid", "Unpaid"
        CANCELED = "canceled", "Canceled"
        REFUNDED = "refunded", "refunded"

    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="invoices")
    due_date = models.DateTimeField(default=timezone.now() + timedelta(days=15))
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UNPAID)
    pdf_file = models.FileField(upload_to="invoices/")

    history = HistoricalRecords()


    def __str__(self):
        return f"Invoice: {self.shipment.id} - {self.shipment.title}"