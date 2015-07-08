from django import forms
from main.models import Document, Projects, Project_Settings

class DocumentForm(forms.ModelForm):
    docfile = forms.FileField(label='', help_text='Please select a file and click the Upload button. Supported file format accepted: *.mzXML')
    class Meta:
        model = Document
        fields = ('Concentration',)

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('Project_Name',)

class NewSettingForm(forms.ModelForm):
    class Meta:
        model = Project_Settings
        fields = ('Settings_Name','Mass_Over_Charge',)


class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = []

