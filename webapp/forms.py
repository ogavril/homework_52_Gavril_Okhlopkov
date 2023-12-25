from django import forms
from webapp.models import List, Project


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['summary', 'description', 'status', 'type']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start', 'end']
        labels = {'name': 'Название', 'description': 'Описание', 'start': 'Дата начала', 'end': 'Дата конца'}


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
