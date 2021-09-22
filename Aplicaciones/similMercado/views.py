from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usuario,Producto,Categoria,Vendedor
from .serializers import UsuarioSerializer,ProductoSerializer,VendedorSerializer,CategoriaSerializer


# Create your views here.

def index(request):
    return render(request,"similMercado/index.html")

### USUARIOS ###
@api_view(['GET'])
def usuariosList(request):
	usuarios = Usuario.objects.all().order_by('id')
	serializer = UsuarioSerializer(usuarios,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def usuariosDetail(request, pk):
	usuarios = Usuario.objects.get(id=pk)
	serializer =  UsuarioSerializer(usuarios, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def usuarioCreate(request):
	serializer = UsuarioSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def usuarioUpdate(request, pk):
	usuario = Usuario.objects.get(id=pk)
	serializer = UsuarioSerializer(instance=usuario, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def usuarioDelete(request, pk):
	usuario = Usuario.objects.get(id=pk)
	usuario.delete()
	return Response('Usuario Borrado Correctamente')

### PRODUCTOS ###
@api_view(['GET'])
def productosList(request):
	productos = Producto.objects.all().order_by('id')
	serializer = ProductoSerializer(productos,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def productosDetail(request, pk):
	productos = Producto.objects.get(id=pk)
	serializer =  ProductoSerializer(productos, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def productosCreate(request):
	serializer = ProductoSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def productosUpdate(request, pk):
	producto = Producto.objects.get(id=pk)
	serializer = ProductoSerializer(instance=producto, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def productosDelete(request, pk):
	producto = Producto.objects.get(id=pk)
	producto.delete()
	return Response('Producto Borrado Correctamente')

### VENDEDORES ###
@api_view(['GET'])
def vendedoresList(request):
	vendedores = Vendedor.objects.all().order_by('id')
	serializer = VendedorSerializer(vendedores,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def vendedoresDetail(request, pk):
	vendedores = Vendedor.objects.get(id=pk)
	serializer =  VendedorSerializer(vendedores, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def vendedoresCreate(request):
	serializer = VendedorSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def vendedoresUpdate(request, pk):
	vendedor = Vendedor.objects.get(id=pk)
	serializer = VendedorSerializer(instance=vendedor, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def vendedoresDelete(request, pk):
	vendedor = Vendedor.objects.get(id=pk)
	vendedor.delete()
	return Response('Vendedor Borrado Correctamente')