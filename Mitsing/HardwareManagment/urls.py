from django.contrib import admin
from django.urls import path
from HardwareManagment.views import *

app_name = 'Home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='Home'),
    path('print/', PrintView.as_view(), name='print'),
    path('maintenance/', MaintenanceView.as_view(), name='maintenance'),
    path('users/', UsersView.as_view(), name='users'),
    path('hardware/', HardwareView.as_view(), name='hardware'),
    path('ventors/', VentorsView.as_view(), name='ventors'),
    path('pdf/<int:pk>', PdfView.as_view(), name='pdf')
]