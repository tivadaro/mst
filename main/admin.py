from django.contrib import admin
from main.models import Document, Project_Settings, Projects

# Register your models here.
admin.site.register(Document)
admin.site.register(Projects)

class Project_SettingsAdmin(admin.ModelAdmin):
    #fields = ('pk', 'Settings_Name')
    list_display = ('pk', 'Settings_Name', 'User_ID') #You can use 'pk' or 'id'

admin.site.register(Project_Settings, Project_SettingsAdmin)
