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
            status=request.POST.get('status'),
            due_date=request.POST.get('due_date'),
        )
        return HttpResponseRedirect('/')
