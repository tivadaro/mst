from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
import sys, os
import base64
import struct
import xml.parsers.expat

#Organization: Users, Projects, Settings, Files, Permissions classes etc.
class Project_Settings(models.Model): #The Project_ID is generated automatically and can be reffered as models.ForeignKey(TableName)
    Settings_Name=models.CharField(max_length=100)
    User_ID=models.IntegerField(default=1)
    Mass_Over_Charge=models.DecimalField(max_digits=13,decimal_places=9,default=0)

class Test_File(models.Model):
    Mass_Over_Charge=models.DecimalField(max_digits=13,decimal_places=9,default=0)
    Concentration=models.DecimalField(max_digits=13,decimal_places=9,default=0) #Establish the actual concetration - maybe decide to use pmol injected?

class Projects(models.Model):
    Project_Name=models.CharField(max_length=100)
    Setting_ID=models.ForeignKey(Project_Settings, null=True, blank=True,on_delete=models.SET_NULL)
    User_ID=models.IntegerField(default=0)
    Test_ID=models.ForeignKey(Test_File, null=True, blank=True,on_delete=models.SET_NULL)
    def __str__(self):              # __unicode__ on Python 2
        return self.Project_Name

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return 'user_{0}/{1}'.format(instance.user.id, filename)
    return '/'.join(['documents', str(instance.Setting_ID.pk), filename])

class Document(models.Model):
    docfile=models.FileField(upload_to=user_directory_path)
    file_name=models.CharField(max_length=100, default = '')
    Setting_ID=models.ForeignKey(Project_Settings, null=True, blank=True,on_delete=models.SET_NULL)
    Concentration=models.DecimalField(max_digits=13,decimal_places=9,default=0) #Establish the actual concetration - maybe decide to use pmol injected?
    #def folder_of_loggedin_user_exists: Chek if the loggedin user has a folder in the main documents folder
    #return True

class Standard_Curve_Report(models.Model):
    Report=models.CharField(max_length=200)
    Setting_ID=models.ForeignKey(Project_Settings, null=True, blank=True,on_delete=models.SET_NULL)

#mzXML specific MS, MS/MS classes
class MSScan():
    def __init__(self):
        self.id = 0
        self.retention_time = 0.0
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
        self.precursorCharge = 0 #Remove it? This may or may not be in the mzxml file

class mzXML():
    def __init__(self): #these variables are specific for each instance of mzXML since they are in the __init__() method
        self.msLevel = 0
        self.current_tag = ''
        self.tag_level = 0
        self.MS1_list = []
        self.MS2_list = []

    def decode_spectrum(self,line):
        decoded = base64.standard_b64decode(line)
        tmp_size = len(decoded)/4
        unpack_format1 = ">%dL" % tmp_size
        idx = 0
        mz_list = []
        intensity_list = []
        for tmp in struct.unpack(unpack_format1,decoded):
            tmp_i = struct.pack("I",tmp)
            tmp_f = struct.unpack("f",tmp_i)[0]
            if( idx % 2 == 0 ):
                mz_list.append( float(tmp_f) )
            else:
                intensity_list.append( float(tmp_f) )
            idx += 1
        return mz_list,intensity_list

    def _start_element(self,name,attrs): #name is the name of the specific instance.
        self.tag_level += 1
        self.current_tag = name
        if( name == 'precursorMz' ):
            self.MS2_list[-1].precursor_intensity = float(attrs['precursorIntensity'])
            self.MS2_list[-1].precursor_charge = 0
            #if( attrs.has_key('precursorCharge') ):
            #    self.MS2_list[-1].precursor_charge = int(attrs['precursorCharge'])
        if( name == 'scan' ):
            self.msLevel = int(attrs['msLevel'])
            if( self.msLevel == 1 ):
                tmp_ms = MS1Scan()
                #print ("I am reading a line that is an MS 1 scan")
            elif( self.msLevel == 2 ):
                tmp_ms = MS2Scan()
                #print ("I am reading a line that is a MS 2 scan")
            else:
                print ("What is it?",attrs)
                sys.exit(1)
            tmp_ms.id = int(attrs['num'])
            tmp_ms.retention_time = float(attrs['retentionTime'].strip('PTS'))
            tmp_ms.mz_list = []
            tmp_ms.intensity_list = []
            if( self.msLevel == 1 ):
                self.MS1_list.append(tmp_ms)
            elif( self.msLevel == 2 ):
                tmp_ms.ms1_id = self.MS1_list[-1].id
                self.MS2_list.append(tmp_ms)

    def _end_element(self,name):
        #self.msLevel = 0 If this is reset every time the MS2 list is never filled
        self.tag_level -= 1
        self.current_tag = ''

    def _char_data(self,data):
        if( self.current_tag == 'precursorMz' ):
            #print("This is the data to be converted to float%s:\n",data)
            self.MS2_list[-1].precursor_mz = float(data)
        if( self.current_tag == 'peaks' ):
            mz_list, intensity_list = self.decode_spectrum(data)
            #mz_string = b''.join((struct.pack('>f',i) for i in mz_list))
            #intensity_string = b''.join((struct.pack('>f',i) for i in intensity_list))
            if( self.msLevel == 1 ):
                self.MS1_list[-1].mz_list += mz_list
                self.MS1_list[-1].intensity_list += intensity_list
            elif( self.msLevel == 2 ):
                self.MS2_list[-1].mz_list = mz_list
                self.MS2_list[-1].intensity_list = intensity_list

    def parse_file(self,filename_mzXML):
        mzXML_file = open(filename_mzXML,'r')
        mzXML_file_content = ''
        for each_line in mzXML_file:
            mzXML_file_content += each_line
        mzXML_file.close()
        #print("This is the value of contentXML",mzXML_file_content)
        expat = xml.parsers.expat.ParserCreate()        #start a new parser
        expat.buffer_size=20000
        expat.StartElementHandler = self._start_element #define the Start element handler?
        expat.EndElementHandler = self._end_element     #define the End elemnet handler
        expat.CharacterDataHandler = self._char_data    #define the character handler
        expat.Parse(mzXML_file_content)
        sys.stderr.write("Done\n")