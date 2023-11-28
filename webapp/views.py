from django.shortcuts import render
from webapp.models import List


# Create your views here.


def index_view(request):
    lists = List.objects.all
    return render(request, 'index.html', {'lists': lists})
