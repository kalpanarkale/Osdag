# Generated by Django 4.2.1 on 2023-05-10 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finplatedesign',
            name='fin_plate_design_report',
        ),
        migrations.RemoveField(
            model_name='finplatedesignreport',
            name='fin_plate_design',
        ),
    ]
