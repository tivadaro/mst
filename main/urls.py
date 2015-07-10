from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^about/$',  views.about_mst),
    url(r'^graph/$',  views.graph_mst),
    url(r'^help/$',  views.help_mst),
    url(r'^project/(?P<Project_ID>[0-9]+)/$',  views.project_detail),
    url(r'^project/(?P<Project_ID>[0-9]+)/link_project_to_setting/$',  views.link_project_to_setting),
    url(r'^project/(?P<Project_ID>[0-9]+)/link_project_to_setting/(?P<Setting_ID>[0-9]+)/$',  views.link_project_to_setting_save),
    url(r'^setting/(?P<Setting_ID>[0-9]+)/$',  views.setting_detail),
    url(r'^project_delete/(?P<Project_ID>[0-9]+)/$',  views.project_delete),
    url(r'^setting_delete/(?P<Setting_ID>[0-9]+)/$',  views.setting_delete),
    url(r'^upload_setting_files/(?P<Setting_ID>[0-9]+)/$',  views.upload_setting_files, name ='upload_setting_files'),
    url(r'^projects/$',  views.projects_mst),
    url(r'^settings/$',  views.project_settings),
    url(r'^new_project/$',  views.new_project_name, name='new_project_name'),
    url(r'^new_setting/$',  views.new_setting_name, name='new_setting_name'),
]