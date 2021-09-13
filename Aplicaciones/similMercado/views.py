from Aplicaciones.similMercado.models import Usuario
from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    usuarios = Usuario.objects.filter(activo = True)
    return render(request,"similMercado/home.html",{'usuarios':usuarios})