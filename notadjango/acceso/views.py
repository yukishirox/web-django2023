from django.shortcuts import render
from tienda.models import *

def acceso_login(request):
 form= Producto.objects.filter(estado_id=1, producto_categoria_id=1).order_by('-id').all()
 return render(request, 'acceso/login.html', {'form': form})
