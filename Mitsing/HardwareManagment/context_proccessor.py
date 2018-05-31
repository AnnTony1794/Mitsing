from django.shortcuts import render
from HardwareManagment.models import *

def context(request):
	emp = Employee.objects.all()

	objs = [emp]
	return {'objs': objs}