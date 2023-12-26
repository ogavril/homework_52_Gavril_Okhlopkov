from django.db.models import Q
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Project, List
from ..forms import ProjectForm, SimpleSearchForm


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(name__icontains=self.search_value) |
                                       Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail_project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = List.objects.filter(project=self.object).order_by('-created_at')
        return context


class ProjectCreateView(CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.id})


class ProjectUpdateView(UpdateView):
    template_name = 'projects/project_update.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse_lazy('project', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'projects/delete_project.html'
    model = Project
    success_url = reverse_lazy('projects')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.is_deleted:
            self.object.is_deleted = True
            self.object.save()
            return super().delete(request, *args, **kwargs)
