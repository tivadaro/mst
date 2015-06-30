from django import forms
from main.models import Projects, Project_Settings

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

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

