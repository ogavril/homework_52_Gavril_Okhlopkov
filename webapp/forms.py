from django import forms
from webapp.models import List, Project


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['summary', 'description', 'status', 'type', 'project']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start', 'end']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
