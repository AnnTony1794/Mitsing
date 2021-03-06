from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Hardware(models.Model):
    name = models.CharField(max_length=50)
    type_of_hardware = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    os = models.CharField(max_length=40)
    cpu_name = models.CharField(max_length=50)
    cpu_capacity = models.IntegerField()
    ram_capacity = models.IntegerField()
    hard_disk_capacity = models.IntegerField()
    date_discard = models.DateField(null=True, blank=True)
    net_access = models.BooleanField()
    office_software = models.CharField(max_length=50)
    antivirus_software = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Bills(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    hardware = models.ManyToManyField(Hardware)
    create = models.DateField()
    arrive = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Department(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    badge = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    hardware = models.ManyToManyField(Hardware)

    context_object_name = 'employee_list'
    def __str__(self):
        return self.name


class Maintenance(models.Model):
    hardware = models.ForeignKey(Hardware, on_delete=models.SET_NULL, null=True, blank=True)
    schedule_date = models.DateField()
    made_date = models.DateField(null=True, blank=True)
    employee_in_chage = models.ForeignKey(Employee, on_delete=models.CASCADE)


    context_object_name = 'maintenance_list'
    def __str__(self):
        return str(self.id)