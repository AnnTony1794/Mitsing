from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Vendor)
admin.site.register(Bills)
admin.site.register(Hardware)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Maintenance)
