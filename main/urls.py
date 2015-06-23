from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^about/$',  views.about_mst),
    url(r'^help/$',  views.help_mst),
    #url(r'^new_project/$',  views.new_project_mst),
    url(r'^projects/$',  views.projects_mst),
    url(r'^settings/$',  views.project_settings),
    url(r'^new_project/$',  views.new_project_name, name='new_project_name'), #<-up to here these urls are for the main app (they should be grouped accordingly?
]