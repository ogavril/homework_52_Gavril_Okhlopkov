from django import forms
from webapp.models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['summary', 'description', 'status', 'type']
