from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

class Document(models.Model):
    docfile=models.FileField(upload_to='documents/%Y/%m/%d')

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