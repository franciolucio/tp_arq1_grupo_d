from Aplicaciones.similMercado.models import Usuario
from django.shortcuts import render
from .models import Usuario,Producto

# Create your views here.
def home(request):
    productos = Producto.objects.filter(activo = True)
    return render(request,"similMercado/home.html",{'productos':productos})