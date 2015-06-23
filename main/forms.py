from django import forms
from main.models import Projects

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class NewProjectForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ('Project_Name',)