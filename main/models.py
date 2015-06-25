from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
import sys, os
import base64
import struct
import xml.parsers.expat

class Document(models.Model):
    docfile=models.FileField(upload_to='documents/%Y/%m/%d')
    #def folder_of_loggedin_user_exists: Chek if the loggedin user has a folder in the main documents folder
    #    return True
#Organization: Users, Projects, Settings, Files, Permissions classes etc.
class Project_Settings(models.Model): #The Project_ID is generated automatically and can be reffered as models.ForeignKey(TableName)
    Settings_Name=models.CharField(max_length=100)
    User_ID=models.IntegerField(default=1)

class Test_File(models.Model):
    File_Name=models.CharField(max_length=100)
    File_Location=models.CharField(max_length=100)
    Mass_Over_Charge=models.DecimalField(max_digits=5,decimal_places=3)
    Concentration=models.DecimalField(max_digits=5,decimal_places=3) #Establish the actual concetration - maybe decide to use pmol injected?

class Standard_Curve_Report(models.Model):
    Report=models.CharField(max_length=200)

class Setting_File(models.Model):
    File_Name=models.CharField(max_length=100)
    File_Location=models.CharField(max_length=100)
    Mass_Over_Charge=models.DecimalField(max_digits=5,decimal_places=3)
    Concentration=models.DecimalField(max_digits=5,decimal_places=3) #Establish the actual concetration - maybe decide to use pmol injected?
    Standard_Curve_Report_ID=models.ForeignKey(Standard_Curve_Report)

class Projects(models.Model):
    Project_Name=models.CharField(max_length=100)
    Setting_ID=models.IntegerField(default=0)
    User_ID=models.IntegerField(default=0)
    Test_ID=models.IntegerField(default=0)

#mzXML specific MS, MS/MS classes
class MSScan():
    def __init__(self):
        self.id = 0
        self.peak_count = 0
        self.filter_line = ''
        self.retention_time = 0.0
        self.low_mz = 0.0
        self.high_mz = 0.0
        self.base_peak_mz = 0.0
        self.base_peak_intensity = 0.0
        self.total_ion_current = 0.0
        self.list_size = 0
        self.encoded_mz = ''
        self.encoded_intensity = ''
        self.mz_list = []
        self.intensity_list = []

class MS1Scan(MSScan):
    def __init__(self):
        pass

class MS2Scan(MSScan):
    def __init__(self):
        self.ms1_id = 0
        self.precursor_mz = 0.0
        self.precursor_intensity = 0.0
        self.precursorCharge = 0

