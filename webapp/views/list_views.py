from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import List
from django.views.generic import TemplateView, View, FormView
from webapp.forms import ListForm


# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        lists = List.objects.all()
        return render(request, 'lists/index.html', {'lists': lists})


class ListCreateView(FormView):
    template_name = 'lists/add_list.html'
    form_class = ListForm

    def form_valid(self, form):
        self.list = form.save()
        return redirect('show', pk=self.list.pk)


class ListDeleteView(View):
    def get(self, request, *args, **kwargs):
        lists = get_object_or_404(List, pk=kwargs.get('pk'))
        return render(request, 'lists/delete_list.html', {'lists': lists})

    def post(self, request, *args, **kwargs):
        lists = get_object_or_404(List, pk=kwargs.get('pk'))
        lists.delete()
        return redirect('index')


class ListView(TemplateView):
    template_name = 'lists/detail_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = get_object_or_404(List, pk=kwargs.get('pk'))
        return context


class ListUpdateView(FormView):
    template_name = 'lists/update_list.html'
    form_class = ListForm

    def dispatch(self, request, *args, **kwargs):
        self.lists = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(List, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.lists
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('show', pk=self.lists.pk)
