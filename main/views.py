from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import Context
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime
import os,sys
import json
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from main.forms import DocumentForm, NewProjectForm, NewSettingForm, DeleteNewForm
from main.models import Document, Projects, Project_Settings, MSScan, MS1Scan, MS2Scan, mzXML
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required
def project_settings(request):
   if request.user.is_authenticated():
       Settings_List=Project_Settings.objects.filter(User_ID = request.user.pk).order_by('-pk') #Filter for logged in user and order so latest is first (using the reverse order of the primary key: '-pk')
       #Project_List=Projects.objects.filter(User_ID = request.user.pk).filter(Setting_ID__gt = 0)
       #Only send the project list of the logged in user and have setting assigned
       #(i.e., Setting_ID>0. For this yoiu must use Setting_ID__gt=0? weird!
       paginator = Paginator(Settings_List, 10)
       # Show 5 projects per page. Maybe offer an account settings where this chan be changed?
       page = request.GET.get('page')
       try:
            Numbered_Settings_List = paginator.page(page)
       except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            Numbered_Settings_List = paginator.page(1)
       except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            Numbered_Settings_List = paginator.page(paginator.num_pages)
       return render(request,'main/settings.html',{'username': request.user.username, 'Settings_List': Numbered_Settings_List})

@login_required
def new_setting_name(request):
   if request.user.is_authenticated():
        if request.method == "POST":
            form = NewSettingForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.User_ID = request.user.pk
                post.Mass_Over_Charge=form.cleaned_data['Mass_Over_Charge']
                post.save()
                return redirect('main.views.project_settings')
        else:
            form = NewSettingForm()
        Settings_List=Project_Settings.objects.filter(User_ID = request.user.pk).order_by('-pk') #Only send the project list of the logged in user and sort for - primary key (latest =first)
        return render(request, 'main/edit_setting.html', {'username': request.user.username, 'Settings_List': Settings_List, 'form': form})

@login_required
def new_setting_mst(request):
   if request.user.is_authenticated():
       form = DocumentForm()
       Settings_List=Project_Settings.objects.filter(User_ID = request.user.pk).order_by('-pk') #Only send the project list of the logged in user
       return render(request,'main/new_setting.html',{'username': request.user.username, 'Settings_List': Settings_List, 'form': form} )

@login_required
def about_mst(request):
   if request.user.is_authenticated():
       return render(request,'main/about.html',{'username': request.user.username} )


@login_required
def new_project_mst(request):
   if request.user.is_authenticated():
       Project_List=Projects.objects.filter(User_ID = request.user.pk).order_by('-pk') #Only send the project list of the logged in user
       return render(request,'main/new_project.html',{'username': request.user.username, 'Project_List': Project_List} )

@login_required
def new_project_name(request):
   if request.user.is_authenticated():
        if request.method == "POST":
            form = NewProjectForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.User_ID = request.user.pk
                post.save()
                return redirect('main.views.projects_mst')
        else:
            form = NewProjectForm()
        Project_List=Projects.objects.filter(User_ID = request.user.pk).order_by('-pk') #Only send the project list of the logged in user and sort for - primary key (latest =first)
        return render(request, 'main/edit_project.html', {'username': request.user.username, 'Project_List': Project_List, 'form': form})


@login_required
def projects_mst(request):
   if request.user.is_authenticated():
       Project_List=Projects.objects.filter(User_ID = request.user.pk).order_by('-pk') #Filter for logged in user and order so latest is first (using the reverse order of the primary key: '-pk')
       #Project_List=Projects.objects.filter(User_ID = request.user.pk).filter(Setting_ID__gt = 0)
       #Only send the project list of the logged in user and have setting assigned
       #(i.e., Setting_ID>0. For this yoiu must use Setting_ID__gt=0? weird!
       paginator = Paginator(Project_List, 10)
       # Show 5 projects per page. Maybe offer an account settings where this chan be changed?
       page = request.GET.get('page')
       try:
            Numbered_Project_List = paginator.page(page)
       except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            Numbered_Project_List = paginator.page(1)
       except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            Numbered_Project_List = paginator.page(paginator.num_pages)
       return render(request,'main/projects.html',{'username': request.user.username, 'Project_List': Numbered_Project_List})


#@login_required
#def setting_file_detail(request,Setting_ID, File_Name):
#   if request.user.is_authenticated():
#       #Settings_List=Project_Settings.objects.filter(User_ID = request.user.pk).filter(pk = Setting_ID) #get the project ID of the user and from the /project/id request
#        #filename_mzXML = os.path.join('/home/tivi/mst/media/documents/34/', File_Name)
#        filename_mzXML = '/home/tivi/mst/media/documents/34/CMS1MS2.mzXML'
#        if( not os.access(filename_mzXML,os.R_OK) ):
#            print ("%s is not accessible."%filename_mzXML)
#        mzXMLo = mzXML()
#        mzXMLo.parse_file(filename_mzXML)
#        f_out = open(filename_mzXML+'.ms1','w')
#        for tmp_ms1 in mzXMLo.MS1_list:
#            #f_out.write("S\t%06d\t%06d\n"%(tmp_ms1.id, tmp_ms1.id))
#            #f_out.write("I\tRetTime\t%.2f\n"%(tmp_ms1.retention_time))
#            f_out.write("RT\t%.2f\n"%(tmp_ms1.retention_time))
#            for i in range(0,len(tmp_ms1.mz_list)):
#                f_out.write("%f\t%.2f\t0\n"%(tmp_ms1.mz_list[i],tmp_ms1.intensity_list[i]))
#        f_out.close()
#        return render(request,'main/setting_file_detail.html',{'username': request.user.username, 'File_Name':File_Name, "Setting_ID":Setting_ID } )

@login_required
def project_detail(request, Project_ID):
   if request.user.is_authenticated():
       Project_List=Projects.objects.filter(User_ID = request.user.pk).filter(pk = Project_ID) #get the project ID of the user and from the /project/id request
       return render(request,'main/project_detail.html',{'username': request.user.username, 'Project_List': Project_List} )

@login_required
def link_project_to_setting (request, Project_ID):
   if request.user.is_authenticated():
       Project_List=Projects.objects.filter(User_ID = request.user.pk).filter(pk = Project_ID) #get the project ID of the user and from the /project/id request
       #return render(request,'main/project_detail.html',{'username': request.user.username, 'Project_List': Project_List} )
       Settings_List=Project_Settings.objects.filter(User_ID = request.user.pk).order_by('-pk') #Filter for logged in user and order so latest is first (using the reverse order of the primary key: '-pk')
       #Project_List=Projects.objects.filter(User_ID = request.user.pk).filter(Setting_ID__gt = 0)
       #Only send the project list of the logged in user and have setting assigned
       #(i.e., Setting_ID>0. For this yoiu must use Setting_ID__gt=0? weird!
       paginator = Paginator(Settings_List, 10)
       # Show 5 projects per page. Maybe offer an account settings where this chan be changed?
       page = request.GET.get('page')
       try:
            Numbered_Settings_List = paginator.page(page)
       except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            Numbered_Settings_List = paginator.page(1)
       except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            Numbered_Settings_List = paginator.page(paginator.num_pages)
       return render(request,'main/link_project_to_setting.html',{'username': request.user.username, 'Settings_List': Numbered_Settings_List, 'Project_List': Project_List})

@login_required
def link_project_to_setting_save (request, Project_ID, Setting_ID):
   if request.user.is_authenticated():
       Project_List=Projects.objects.filter(pk = Project_ID).filter(User_ID = request.user.pk) #get the project ID of the user and from the /project/id request
       Setting = Project_Settings(pk = Setting_ID)
       #Attach it to the update_curent_project_with_new_setting_ID object by setting the Projects.Setting_ID to Setting (the instance)
       #update_curent_project_with_new_setting_ID = Projects(Setting_ID = Setting)
       #update_curent_project_with_new_setting_ID = Projects(pk = Project_ID)
       for update_curent_project_with_new_setting_ID in Project_List:
           update_curent_project_with_new_setting_ID.Setting_ID = Setting
           update_curent_project_with_new_setting_ID.save()
       #Requerry the newly saved Project List
       Project_List=Projects.objects.filter(pk = Project_ID).filter(User_ID = request.user.pk)
       return render(request,'main/project_detail.html',{'username': request.user.username, 'Project_List': Project_List} )

@login_required
def setting_detail(request, Setting_ID):
   if request.user.is_authenticated():
       Settings_List=Project_Settings.objects.filter(User_ID = request.user.pk).filter(pk = Setting_ID) #get the project ID of the user and from the /project/id request
       documents = Document.objects.filter(Setting_ID=Setting_ID)
       #prepare the chromatograms data using the file names from documents
       #Get the m/z of the current Setting_ID
       #the data has to be the MS/MS of the ion we defined in the Setting.
       Mass_Over_Charge_List=Project_Settings.objects.filter(User_ID = request.user.pk).filter(pk = Setting_ID)
       for setting_ion_item in Mass_Over_Charge_List:
           setting_ion=setting_ion_item.Mass_Over_Charge
       #We need to get the max absolute intensity of the whole run. This will be our 100%
       chromatogram=[]
       chromatogram.append([])
       chromatogram[0].append('Time')
       for document_item in documents: #Append the filenames to distinguis chromatograms
           chromatogram[0].append(str(document_item.file_name))
       #return render(request,'main/setting_detail.html',{'username': request.user.username, 'Settings_List': Settings_List, 'documents': documents,'setting_ion':setting_ion})

       #Take the first file and populate the retention time and the intensity
       for document_item in documents:
            filename_mzXML= '/'.join(['/home/tivi/mst/media/documents', str(Setting_ID), document_item.file_name])
            if( not os.access(filename_mzXML,os.R_OK) ):
                print ("%s is not accessible."%filename_mzXML)
            print("These are the documents that I will read and workon %s",filename_mzXML)
            #filename_mzXML contains the path for each file
            mzXMLo = mzXML()
            mzXMLo.parse_file(filename_mzXML)
            j=1
            for tmp_ms1 in mzXMLo.MS1_list:
                chromatogram.append([])
                chromatogram[j].append(format(tmp_ms1.retention_time, '.1f')) #Data in the mzXML files is saved in seconds
                chromatogram[j].append(max(tmp_ms1.intensity_list)) #Gets the highest intensity of all peaks
                #print("This is the intensity list of %s\n",(tmp_ms1.retention_time)/60,*tmp_ms1.intensity_list)
                j=j+1
            #By now we have two columns filled. Next each file will only populate one column (with the mz_list). The retention time is the same in all files???
            #Unfortunately the retention time is not the same in all files. So before we can show all chromatograms in the same graph
            #This needs be solved
            #document_number=len(documents) #The number of files that need to be processed and added to the chromatogram list
            #print("This is the document number%d\n", document_number)
            #for index in range (1,document_number):
        #    document_item = documents[index]
        #   filename_mzXML= '/'.join(['/home/tivi/mst/media/documents', str(Setting_ID), document_item.file_name])
        #   if( not os.access(filename_mzXML,os.R_OK) ):
        #       print ("%s is not accessible."%filename_mzXML)
        #   print("These are the documents that I will add to the existing list %s\n",filename_mzXML)
        #   mzXMLo = mzXML()
        #   mzXMLo.parse_file(filename_mzXML)
        #   j=1
        #   for tmp_ms1 in mzXMLo.MS1_list:
        #       chromatogram.append([])
        #       chromatogram[j].append(max(tmp_ms1.intensity_list)) #Gets the highest intensity of all peaks
        #       j=j+1
       return render(request,'main/setting_detail.html',{'username': request.user.username, 'Settings_List': Settings_List, 'documents': documents,'setting_ion':setting_ion})

@login_required
def project_delete(request, Project_ID):
   if request.user.is_authenticated():
       Project_List=Projects.objects.filter(User_ID = request.user.pk).filter(pk = Project_ID).delete() #get and delete the project ID of the user and from the /project/id request
       return redirect('main.views.projects_mst')


@login_required
def setting_delete(request, Setting_ID):
   if request.user.is_authenticated():
       Settings_List=Project_Settings.objects.filter(User_ID = request.user.pk).filter(pk = Setting_ID).delete() #get and delete the Settings ID of the user and from the /project/id request
       return redirect('main.views.project_settings')


@login_required
def upload_setting_files(request, Setting_ID):
   if request.user.is_authenticated():
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = form.save(commit=False) #do not save the from
            # Setting ID of Document is the foreign key for Project_Settings
            #Get and instance of the Project_Setting thet we get from the second param of the view
            Setting = Project_Settings(pk = Setting_ID)
            #Attach it to the newdoc object by setting the Document.Setting_ID to Setting (the instance)
            newdoc = Document(docfile = request.FILES['docfile'], Setting_ID = Setting)
            newdoc.Concentration = form.cleaned_data['Concentration']
            newdoc.file_name=request.FILES['docfile'].name
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect('')
    else:
        form = DocumentForm() # A empty, unbound form
    # Load documents for the list page
    documents = Document.objects.filter(Setting_ID=Setting_ID)
    # Render list page with the documents and the form
    return render_to_response('main/upload_setting_files.html', {'documents': documents, 'form': form}, context_instance=RequestContext(request))



@login_required
def help_mst(request):
   if request.user.is_authenticated():
       return render(request,'main/help.html',{'username': request.user.username} )

@login_required
def graph_mst(request, Setting_ID, File_Name):
   if request.user.is_authenticated():
        #data format for the graph
        #data=    [['Concentration', 'Intensity'],
        #          [ 8,      12],
        #          [ 4,      5.5],
        #          [ 11,     14],
        #          [ 4,      5],
        #          [ 3,      3.5],
        #          [ 6.5,    7]]
        #filename_mzXML = '/home/tivi/mst/media/documents/34/CMS1MS2.mzXML'
        filename_mzXML= '/'.join(['/home/tivi/mst/media/documents', str(Setting_ID), File_Name])
        if( not os.access(filename_mzXML,os.R_OK) ):
            print ("%s is not accessible."%filename_mzXML)
        mzXMLo = mzXML()
        mzXMLo.parse_file(filename_mzXML)

        #Get the m/z of the current Setting_ID
        #the data has to be the MS/MS of the ion we defined in the Setting.
        Mass_Over_Charge_List=Project_Settings.objects.filter(User_ID = request.user.pk).filter(pk = Setting_ID)
        for setting_ion_item in Mass_Over_Charge_List:
            setting_ion=setting_ion_item.Mass_Over_Charge

        #We need to get the max absolute intensity of the whole run. This will be our 100%
        chromatogram=[]
        chromatogram.append([])
        chromatogram[0].append('Time')
        chromatogram[0].append('Relative initensity (%)')
        #data1=[]
        #data1.append([])
        #data1[0].append('m/z')
        #data1[0].append('Relative initensity (%)')
        data=[]
        data.append([])
        data[0].append('m/z')
        data[0].append('Relative initensity (%)')

        j=1
        for tmp_ms1 in mzXMLo.MS1_list:
            chromatogram.append([])
            chromatogram[j].append(tmp_ms1.retention_time/60) #Data in the mzXML files is saved in seconds
            chromatogram[j].append(max(tmp_ms1.intensity_list)) #Gets the highest intensity of all peaks
            j=j+1

        #max_chromatogram_intensity_list=[]
        #max_chromatogram_intensity_list.append([])
        #Normalize the chromatogram intensity list
        #for index in range(1, len(chromatogram)-1):
        #    max_chromatogram_intensity_list[index-1].append(chromatogram[index][1]) #copy the list of all intensities (second position in the chromatogram list)

        #max_chromatogram_intensity = max(max_chromatogram_intensity_list)
        #for index in range (0,len(chromatogram)):
        #    chromatogram[index]=(chromatogram[index]*100)/max_chromatogram_intensity
        file_has_MSMS=False
        if len(mzXMLo.MS2_list)>0:
            file_has_MSMS=True #set this to 0 since there is no MSMS data. This var is used so the MSMS chart is not displayed in graph.html

        tmp_ms2 = mzXMLo.MS2_list[1]
        for i in range(0,len(tmp_ms2.mz_list)):
            data.append([])
            data[i+1].append(tmp_ms2.mz_list[i])
            data[i+1].append(tmp_ms2.intensity_list[i])
        #print ("This is the length of the tmp_ms2 %s\n", len(tmp_ms2))
        #i=0
        #for tmp_ms2 in mzXMLo.MS2_list:
        #    data2.append([])
        #    data2[i+1].append(tmp_ms2.mz_list[i])
        #    data2[i+1].append(tmp_ms2.intensity_list[i])
        #    i=i+1
        return render(request,'main/graph.html',{'username': request.user.username, 'data': json.dumps(data),'chromatogram': json.dumps(chromatogram),'setting_ion': setting_ion,'file_has_MSMS': file_has_MSMS} )
        #return render(request, 'main/graph.html', {'data': json.dumps(data)})


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        # Check if user has designated folder under /media/documents/ -NOT done yet
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/accounts/profile/")
