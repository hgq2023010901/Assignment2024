from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import User, Festival, Date, Calendar

def index(request):
    Festival_list = Festival.objects.all()
    context = {'Festival_list': Festival_list}
    return render(request, 'index.html', context)