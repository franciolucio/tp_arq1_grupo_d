from django.views.decorators import csrf
from Aplicaciones.similMercado.models import Usuario
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Usuario
from .serializers import UsuarioSerializer

# Create your views here.

def index(request):
    return render(request,"similMercado/index.html")

@csrf_exempt
def usuarioApi(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios,many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuarios_serializer = UsuarioSerializer(data=usuario_data)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        return JsonResponse("Fallo al crear usuario",safe=False)
    elif request.method == 'PUT':
        usuario_data = JSONParser().parse(request)
        usuarios = Usuario.objects.get(id=usuario_data['id'])
        usuarios_serializer = UsuarioSerializer(usuarios,data=usuario_data)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return JsonResponse("Actualizado correctamente",safe=False)
        return JsonResponse("Fallo la actualizacion")
    elif request.method == 'DELETE':
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return JsonResponse("Eliminado correctamente",safe=False)