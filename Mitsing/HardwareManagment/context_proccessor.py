from django.shortcuts import render
from HardwareManagment.models import Employee

def context(request):
	emp = Employee.objects.all()
	return {'employees': emp}