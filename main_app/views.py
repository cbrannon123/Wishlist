from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import List

# Create your views here.
def home(request):
    lists = List.objects.all()
    return render(request, 'home.html', {'lists': lists})


class ListCreate(CreateView):
    model = List
    fields = '__all__'
    success_url = '/'

class ListDelete(DeleteView):
    model = List
    fields = '__all__'
    success_url = '/'
