# Generated by Django 2.0.4 on 2018-05-16 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField()),
                ('arrive', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('badge', models.IntegerField()),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HardwareManagment.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type_of_hardware', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=40)),
                ('cpu_name', models.CharField(max_length=50)),
                ('cpu_capacity', models.IntegerField()),
                ('ram_capacity', models.IntegerField()),
                ('hard_disk_capacity', models.IntegerField()),
                ('date_discard', models.DateField(null=True)),
                ('net_access', models.BooleanField()),
                ('office_software', models.CharField(max_length=50)),
                ('antivirus_software', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_date', models.DateField()),
                ('made_date', models.DateField()),
                ('employee_in_chage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HardwareManagment.Employee')),
                ('hardware', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HardwareManagment.Hardware')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='hardware',
            field=models.ManyToManyField(to='HardwareManagment.Hardware'),
        ),
        migrations.AddField(
            model_name='bills',
            name='hardware',
            field=models.ManyToManyField(to='HardwareManagment.Hardware'),
        ),
        migrations.AddField(
            model_name='bills',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HardwareManagment.Vendor'),
        ),
    ]
