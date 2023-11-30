from django.shortcuts import render
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


def delete_list(request):
    list_id = request.GET.get("id")
    for_delete = List.objects.filter(id=list_id)
    for_delete.delete()
    return HttpResponseRedirect('/')
