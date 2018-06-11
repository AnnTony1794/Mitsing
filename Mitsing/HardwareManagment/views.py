from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.conf import settings
from HardwareManagment.models import Employee, Maintenance, Hardware, Vendor
from .filters import PrintFilter, MaintenanceFilter, EmployeeFilter, HardwareFilter, VendorFilter
from django_filters.views import FilterView
# Create your views here.


class HomeView(TemplateView):
    template_name = "HardwareManagment/home.html"


class MaintenanceView(FilterView):
	model = Maintenance
	filterset_class = MaintenanceFilter
	template_name = "HardwareManagment/maintenance.html"
  

class PrintView(FilterView):
	model = Maintenance
	filterset_class = PrintFilter
	template_name = "HardwareManagment/print/print.html"


class UsersView(FilterView):
	model = Employee
	filterset_class = EmployeeFilter
	template_name = "HardwareManagment/users.html"


class HardwareView(FilterView):
	model = Hardware
	filterset_class = HardwareFilter
	template_name = "HardwareManagment/hardware.html"


class VendorsView(FilterView):
	model = Vendor
	filterset_class = VendorFilter
	template_name = "HardwareManagment/vendors.html"


class PdfView(DetailView):
	model = Maintenance
	template_name = "HardwareManagment/print/pdf.html"