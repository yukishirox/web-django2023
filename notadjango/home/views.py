from django.shortcuts import render
from tienda.models import *

def home_inicio(request):
    return render(request, 'home/home.html')
