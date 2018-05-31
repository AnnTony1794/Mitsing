from .models import Maintenance, Employee, Hardware, Vendor
import django_filters
from django import forms

class PrintFilter(django_filters.FilterSet):
    class Meta:
        model = Maintenance
        fields = ['hardware', 'schedule_date', 'employee_in_chage', ]


class MaintenanceFilter(django_filters.FilterSet):
	class Meta:
		model = Maintenance
		fields = ['hardware', 'schedule_date', 'employee_in_chage',]


class EmployeeFilter(django_filters.FilterSet):
	class Meta:
		model = Employee
		fields = ['name', 'badge', 'department',]


class HardwareFilter(django_filters.FilterSet):
	class Meta:
		model = Hardware
		fields = ['name', 'type_of_hardware',]


class VendorFilter(django_filters.FilterSet):
	class Meta:
		model = Vendor
		fields = ['name', 'email', 'phone']