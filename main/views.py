from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.template import Context
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from main.forms import DocumentForm, NewProjectForm
from main.models import Document, Projects, Project_Settings

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


@login_required
def project_settings(request):
    if request.user.is_authenticated():
        # Handle file upload
            form = DocumentForm() # A empty, unbound form
            # Load documents for the list page
            s = Project_Settings.objects.filter(User_ID = request.user.pk) #Only send the list of the Project_setting list of the logged in user
    return render(request,'main/settings.html',{'username': request.user.username, 'settings_html_var': s, 'form': form} )

@login_required
def about_mst(request):
   if request.user.is_authenticated():
       return render(request,'main/about.html',{'username': request.user.username} )

@login_required
def new_project_mst(request):
   if request.user.is_authenticated():
       form = DocumentForm()
       Project_List=Projects.objects.filter(User_ID = request.user.pk) #Only send the project list of the logged in user
       return render(request,'main/new_project.html',{'username': request.user.username, 'Project_List': Project_List, 'form': form} )

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

        Project_List=Projects.objects.filter(User_ID = request.user.pk) #Only send the project list of the logged in user
        return render(request, 'main/edit_project.html', {'username': request.user.username, 'Project_List': Project_List, 'form': form})


@login_required
def projects_mst(request):
   if request.user.is_authenticated():
       Project_List=Projects.objects.filter(User_ID = request.user.pk)
       #Project_List=Projects.objects.filter(User_ID = request.user.pk).filter(Setting_ID__gt = 0)
       #Only send the project list of the logged in user and have setting assigned
       #(i.e., Setting_ID>0. For this yoiu must use Setting_ID__gt=0? weird!
       paginator = Paginator(Project_List, 5)
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
def help_mst(request):
   if request.user.is_authenticated():
       return render(request,'main/help.html',{'username': request.user.username} )

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
    return render(request,'main/loggedin_user_greeter.html',{'username': request.user.username, 'documents': documents, 'form': form} )


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



def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('fileupload.fileuploader_app.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response('main/projects.html', {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )