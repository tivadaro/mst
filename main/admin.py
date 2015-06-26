from django.contrib import admin
from main.models import Document, Project_Settings, Projects

# Register your models here.
admin.site.register(Document)
admin.site.register(Projects)
admin.site.register(Project_Settings)