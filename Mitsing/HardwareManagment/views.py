from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
# Create your views here.


class HomeView(TemplateView):
    template_name = "HardwareManagment/home.html"


class MaintenanceView(TemplateView):
	template_name = "HardwareManagment/maintenance.html"
    
class PrintView(TemplateView):
	template_name = "HardwareManagment/print.html"


class UsersView(TemplateView):
	template_name = "HardwareManagment/users.html"


class HardwareView(TemplateView):
	template_name = "HardwareManagment/hardware.html"


class VentorsView(TemplateView):
	template_name = "HardwareManagment/ventors.html"


class PdfView(TemplateView):
	template_name = "HardwareManagment/pdf.html"