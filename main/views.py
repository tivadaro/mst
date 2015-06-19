from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from main.forms import DocumentForm, NameForm
from main.models import Document, Projects, Project_Settings
# Create your views here.


@login_required
def project_settings(request):
    if request.user.is_authenticated():
        # Handle file upload
            form = DocumentForm() # A empty, unbound form
            # Load documents for the list page
            s = Project_Settings.objects.filter(User_ID = request.user.pk) #Only send the list of the Project_setting list of the logged in user
    return render(request,'settings.html',{'username': request.user.username, 'settings_html_var': s, 'form': form} )

@login_required
def about_mst(request):
   if request.user.is_authenticated():
       return render(request,'about.html',{'username': request.user.username} )

@login_required
def new_project_mst(request):
   if request.user.is_authenticated():
       form = DocumentForm()
       Project_List=Projects.objects.filter(User_ID = request.user.pk) #Only send the project list of the logged in user
       return render(request,'new_project.html',{'username': request.user.username, 'Project_List': Project_List, 'form': form} )

@login_required
def save_new_project_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'post':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_project=Projects(Project_Name = cd['new_project_name'],  User_ID=request.user.pk, Setting_ID=0, Test_ID=0)
            new_project.save()
            return HttpResponseRedirect(r'^about/$')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    #requery the newly updated database with all the projects
    Project_List=Projects.objects.filter(User_ID = request.user.pk)
    return render(request,'projects.html',{'username': request.user.username, 'Project_List': Project_List, 'form': form} )


@login_required
def projects_mst(request):
   if request.user.is_authenticated():
       form = DocumentForm()
       Project_List=Projects.objects.filter(User_ID = request.user.pk) #Only send the project list of the logged in user
       return render(request,'projects.html',{'username': request.user.username, 'Project_List': Project_List, 'form': form} )


@login_required
def help_mst(request):
   if request.user.is_authenticated():
       return render(request,'help.html',{'username': request.user.username} )

@login_required
def main_page_user(request):
    if request.user.is_authenticated():
        # Handle file upload
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile = request.FILES['docfile'])
                newdoc.save()
        #        # Redirect to the document list after POST
        #        return HttpResponseRedirect(reverse('tim.t.views.main_page_user'))
        else:
            form = DocumentForm() # A empty, unbound form
            # Load documents for the list page
            documents = Document.objects.all()
    return render(request,'loggedin_user_greeter.html',{'username': request.user.username, 'documents': documents, 'form': form} )


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/accounts/profile/")