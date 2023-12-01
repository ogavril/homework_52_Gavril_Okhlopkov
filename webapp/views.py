from django.shortcuts import render, get_object_or_404
from webapp.models import List
from django.http import HttpResponseRedirect


# Create your views here.


def index_view(request):
    lists = List.objects.all
    return render(request, 'index.html', {'lists': lists})


def list_add(request):
    if request.method == "GET":
        return render(request, 'add.html')
    elif request.method == "POST":
        List.objects.create(
            description=request.POST.get('description'),
            detailed_descr=request.POST.get('detailed_descr'),
            status=request.POST.get('status'),
            due_date=request.POST.get('due_date'),
        )
        return HttpResponseRedirect('/')


def delete_list(request, pk):
    for_delete = get_object_or_404(List, pk=pk)
    for_delete.delete()
    return HttpResponseRedirect('/')


def show_list(request, pk):
    lists = get_object_or_404(List, pk=pk)
    return render(request, 'detail.html', {'lists': lists})
