# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_document_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting_file',
            name='Standard_Curve_Report_ID',
        ),
        migrations.RemoveField(
            model_name='test_file',
            name='File_Location',
        ),
        migrations.RemoveField(
            model_name='test_file',
            name='File_Name',
        ),
        migrations.AddField(
            model_name='document',
            name='Concentration',
            field=models.DecimalField(max_digits=5, default=0, decimal_places=3),
        ),
        migrations.AddField(
            model_name='project_settings',
            name='Mass_Over_Charge',
            field=models.DecimalField(max_digits=5, default=0, decimal_places=3),
        ),
        migrations.AddField(
            model_name='standard_curve_report',
            name='Setting_ID',
            field=models.ForeignKey(null=True, blank=True, to='main.Project_Settings', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterField(
            model_name='test_file',
            name='Concentration',
            field=models.DecimalField(max_digits=5, default=0, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='test_file',
            name='Mass_Over_Charge',
            field=models.DecimalField(max_digits=5, default=0, decimal_places=3),
        ),
        migrations.DeleteModel(
            name='Setting_File',
        ),
    ]
