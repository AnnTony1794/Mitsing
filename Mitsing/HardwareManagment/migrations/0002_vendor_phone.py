# Generated by Django 2.0.4 on 2018-05-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HardwareManagment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='phone',
            field=models.CharField(default=123, max_length=30),
            preserve_default=False,
        ),
    ]
