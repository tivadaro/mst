from django.contrib import admin

# Register your models here.
from main.models import Document, Project_Settings, Projects


admin.site.register(Document)
admin.site.register(Projects)
admin.site.register(Project_Settings)