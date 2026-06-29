from django.contrib import admin
from ..models import Company


class CompanyInline(admin.StackedInline):
    model = Company
    max_num = 1