from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import List
from django.urls import reverse


# Create your views here.


def index_view(request):
    lists = List.objects.all
    return render(request, 'index.html', {'lists': lists})


def list_add(request):
    if request.method == "GET":
        return render(request, 'add.html')
    elif request.method == "POST":
        due_date_str = request.POST.get('due_date')
        due_date = None if not due_date_str else due_date_str
        List.objects.create(
            description=request.POST.get('description'),
            detailed_descr=request.POST.get('detailed_descr'),
            status=request.POST.get('status'),
            due_date=due_date,
        )
        return redirect(reverse('index'))


def delete_list(request, pk):
    for_delete = get_object_or_404(List, pk=pk)
    for_delete.delete()
    return redirect(reverse('index'))


def show_list(request, pk):
    lists = get_object_or_404(List, pk=pk)
    return render(request, 'detail.html', {'lists': lists})
