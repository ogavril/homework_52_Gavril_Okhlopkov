from django import forms
from django.forms import widgets
from .models import Status, Type


class ListForm(forms.Form):
    summary = forms.CharField(max_length=100, label="Краткое описание")
    description = forms.CharField(max_length=3000, label="Полное описание", widget=widgets.Textarea())
    status = forms.ModelChoiceField(label="Статус", queryset=Status.objects.all())
    type = forms.ModelChoiceField(label="Тип", queryset=Type.objects.all())
