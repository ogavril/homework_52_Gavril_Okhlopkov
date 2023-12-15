from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import List
from django.views.generic import TemplateView, View
from webapp.forms import ListForm


# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        lists = List.objects.all()
        return render(request, 'index.html', {'lists': lists})


class ListCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ListForm()
        return render(request, 'add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ListForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            status = form.cleaned_data.pop('status')
            lists = List.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=status,
                type=types,
            )
            lists.save()
            return redirect('show', pk=lists.pk)
        else:
            return render(request, 'add.html', {'form': form})


class ListDeleteView(View):
    def get(self, request, *args, **kwargs):
        lists = get_object_or_404(List, pk=kwargs.get('pk'))
        return render(request, 'delete_list.html', {'lists': lists})

    def post(self, request, *args, **kwargs):
        lists = get_object_or_404(List, pk=kwargs.get('pk'))
        lists.delete()
        return redirect('index')


class ListView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = get_object_or_404(List, pk=kwargs.get('pk'))
        return context


class ListUpdateView(TemplateView):
    template_name = 'update_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lists = get_object_or_404(List, pk=kwargs.get('pk'))
        form = ListForm(initial={
            'summary': lists.summary,
            'description': lists.description,
            'status': lists.status_id,
            'type': lists.type_id
        })
        context['form'] = form
        context['lists'] = lists
        return context

    def post(self, request, *args, **kwargs):
        lists = get_object_or_404(List, pk=kwargs.get('pk'))
        form = ListForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            status = form.cleaned_data.pop('status')
            lists.summary = form.cleaned_data.get('summary')
            lists.description = form.cleaned_data.get('description')
            lists.status = status
            lists.type = types
            lists.save()
            return redirect('show', pk=lists.pk)
        else:
            return render(request, 'update_list.html', {'form': form})
