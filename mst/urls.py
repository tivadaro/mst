"""tim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from main import views


urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^$', login),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', views.main_page_user),
    url(r'^about/$',  views.about_mst),
    url(r'^help/$',  views.help_mst),
    url(r'^new_project/$',  views.new_project_mst),
    url(r'^projects/$',  views.projects_mst),
    url(r'^settings/$',  views.project_settings),
    url(r'^new_project_name/$',  views.save_new_project_name), #<-up to here these urls are for the main app (they should be grouped accordingly?
    url(r'', include('blog.urls')),
]