from django import forms
from main.models import Projects, Project_Settings

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select an mzXML file please', help_text='This is just a help text to select a file:')


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('Project_Name',)

class NewSettingForm(forms.ModelForm):
    class Meta:
        model = Project_Settings
        fields = ('Settings_Name',)


class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = []

