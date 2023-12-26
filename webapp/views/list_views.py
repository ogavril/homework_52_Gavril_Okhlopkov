from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import List, Project
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from webapp.forms import ListForm


class ListCreateView(CreateView):
    template_name = 'lists/add_list.html'
    form_class = ListForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        list = form.save(commit=False)
        list.project = project
        self.list = form.save()
        return redirect('project', project.pk)


class ListDeleteView(DeleteView):
    model = List

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.project.pk})


class ListView(DetailView):
    model = List
    template_name = 'lists/detail_list.html'
    context_object_name = 'lists'


class ListUpdateView(UpdateView):
    model = List
    template_name = 'lists/update_list.html'
    form_class = ListForm

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.project.pk})
