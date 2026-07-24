from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
from io import BytesIO
from django.core.files.base import ContentFile
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from ..models import Invoice, Shipment
from django.utils import timezone
from datetime import timedelta



class GenerateInvoiceView(View):

    def post(self, request, pk, *args, **kwargs):
        shipment = get_object_or_404(Shipment, id=pk)

        if Invoice.objects.filter(shipment=shipment).exists():
            messages.warning(request, f"Invoice for shipment: {shipment.id} - {shipment.title} already exists.")
            return redirect(request.META.get("HTTP_REFERER", "dispatch"))

        try:
            with transaction.atomic():
                current_date = timezone.now()
                deadline = current_date + timedelta(days=15)

                context = {"shipment": shipment,
                           "created_at": current_date.strftime("%d.%m.%Y."),
                           "due_date": deadline.strftime("%d.%m.%Y.")
                           }

                html_string = render_to_string("invoice_pattern.html", context)

                pdf_buffer = BytesIO()
                pisa_status = pisa.CreatePDF(html_string, dest=pdf_buffer)

                if pisa_status.err:
                    raise Exception("Error during pdf page creations")

                pdf_data = pdf_buffer.getvalue()
                pdf_buffer.close()

                invoice = Invoice(shipment=shipment)
                file_name = f"invoice_shipment_{shipment.id}.pdf"
                invoice.pdf_file.save(file_name, ContentFile(pdf_data),save=True)
            messages.success(request, f"Invoice for {shipment.id} is created successfully.")

        except Exception as e:
            messages.error(request, "Error during invoice creation")

        return redirect(request.META.get("HTTP_REFERER", "dispatch"))
