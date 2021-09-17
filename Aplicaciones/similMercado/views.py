from django.views.decorators import csrf
from Aplicaciones.similMercado.models import Usuario
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Usuario
from .serializers import UsuarioSerializer

# Create your views here.
@csrf_exempt
def usuarioApi(request, id=0):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios,many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)
