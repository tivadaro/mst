# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Settings',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Settings_Name', models.CharField(max_length=100)),
                ('User_ID', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Project_Name', models.CharField(max_length=100)),
                ('Setting_ID', models.IntegerField(default=0)),
                ('User_ID', models.IntegerField(default=0)),
                ('Test_ID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Setting_File',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('File_Name', models.CharField(max_length=100)),
                ('File_Location', models.CharField(max_length=100)),
                ('Mass_Over_Charge', models.DecimalField(max_digits=5, decimal_places=3)),
                ('Concentration', models.DecimalField(max_digits=5, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='Standard_Curve_Report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Report', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Test_File',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('File_Name', models.CharField(max_length=100)),
                ('File_Location', models.CharField(max_length=100)),
                ('Mass_Over_Charge', models.DecimalField(max_digits=5, decimal_places=3)),
                ('Concentration', models.DecimalField(max_digits=5, decimal_places=3)),
            ],
        ),
        migrations.AddField(
            model_name='setting_file',
            name='Standard_Curve_Report_ID',
            field=models.ForeignKey(to='main.Standard_Curve_Report'),
        ),
    ]
