from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^about/$',  views.about_mst),
    url(r'^help/$',  views.help_mst),
    url(r'^terms_of_use/$',  views.terms_of_use_mst),
    url(r'^project/(?P<Project_ID>[0-9]+)/$',  views.project_detail),
    url(r'^project_delete/(?P<Project_ID>[0-9]+)/$',  views.project_delete),
    url(r'^projects/$',  views.projects_mst),
    url(r'^settings/$',  views.project_settings),
    url(r'^new_project/$',  views.new_project_name, name='new_project_name'),
]