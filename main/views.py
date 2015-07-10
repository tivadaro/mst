from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import Context
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime
import os
import json
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from main.forms import DocumentForm, NewProjectForm, NewSettingForm, DeleteNewForm
from main.models import Document, Projects, Project_Settings
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
       return render(request,'main/setting_detail.html',{'username': request.user.username, 'Settings_List': Settings_List, 'documents': documents} )

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
def graph_mst(request):
   if request.user.is_authenticated():
        data=    [['Concentration', 'Intensity'],
                  [ 8,      12],
                  [ 4,      5.5],
                  [ 11,     14],
                  [ 4,      5],
                  [ 3,      3.5],
                  [ 6.5,    7]]
        #return render(request,'main/graph.html',{'username': request.user.username, 'data': json.dumps(data)} )
        return render(request, 'main/graph.html', {'data': json.dumps(data)})

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
