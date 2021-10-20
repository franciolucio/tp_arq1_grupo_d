# # Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from .models import Usuario,Producto,Categoria,Vendedor,Evento
from .serializers import UsuarioSerializer,ProductoSerializer,VendedorSerializer,CategoriaSerializer,EventoSerializer
from rest_framework import status
from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request,"similMercado/index.html")

class Usuarios_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		usuarios = Usuario.objects.filter(activo=True)
		serializer = UsuarioSerializer(usuarios, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UsuarioSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuariosDetails_APIView(APIView):
	def get_object(self, pk):
		try:
			return Usuario.objects.get(pk=pk)
		except Usuario.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		usuario = self.get_object(pk)
		serializer = UsuarioSerializer(usuario)  
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		usuario = self.get_object(pk)
		serializer = UsuarioSerializer(usuario, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		tieneEventos = Evento.objects.filter(id_usuario_comprador=pk).count() > 0
		usuario = self.get_object(pk)
		if tieneEventos:
			usuario.activo = False
			usuario.save()
			return Response(status=status.HTTP_200_OK)
		else:
			usuario.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)

class ProductosConStock_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		productos = Producto.objects.filter(stock__gt=0, activo=True)
		serializer = ProductoSerializer(productos, many=True)
		return Response(serializer.data)

class ProductosCompradoPorUsuario_APIView(APIView):
	def get(self, request, pk, format=None):
		eventos = Evento.objects.filter(id_usuario_comprador=pk)
		serializer = EventoSerializer(eventos, many=True)
		return Response(serializer.data)

class ProductosVendidosPorVendedor_APIView(APIView):
	def get(self, request, pk, format=None):
		id_eventos = []
		eventos = Evento.objects.all()
		for e in eventos:
			if e.id_producto.id_vendedor.id == pk:
				id_eventos.append(e.id)	
		eventosDelVendedor = Evento.objects.filter(id__in=id_eventos)
		serializer = EventoSerializer(eventosDelVendedor, many=True)
		return Response(serializer.data)

class ProductosAsociadosAlVendedor_APIView(APIView):
	def get(self, request, pk, format=None):
		productos = Producto.objects.filter(id_vendedor=pk)
		serializer = ProductoSerializer(productos, many=True)
		return Response(serializer.data)

class Productos_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		productos = Producto.objects.filter(activo=True)
		serializer = ProductoSerializer(productos, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ProductoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductosDetails_APIView(APIView):
	def get_object(self, pk):
		try:
			return Producto.objects.get(pk=pk)
		except Producto.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		producto = self.get_object(pk)
		serializer = ProductoSerializer(producto)  
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		tieneEventos = Evento.objects.filter(id_producto=pk).count() > 0
		producto = self.get_object(pk)
		if tieneEventos:
			producto.activo = False
			producto.save()
			serializer = ProductoSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(status=status.HTTP_200_OK)
		else:
			serializer = ProductoSerializer(producto, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		tieneEventos = Evento.objects.filter(id_producto=pk).count() > 0
		producto = self.get_object(pk)
		if tieneEventos:
			producto.activo = False
			producto.save()
			return Response(status=status.HTTP_200_OK)
		else:
			producto.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)

class Vendedores_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		vendedores = Vendedor.objects.filter(activo=True)
		serializer = VendedorSerializer(vendedores, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = VendedorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendedoresDetails_APIView(APIView):
	def get_object(self, pk):
		try:
			return Vendedor.objects.get(pk=pk)
		except Vendedor.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		vendedor = self.get_object(pk)
		serializer = VendedorSerializer(vendedor)  
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = VendedorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format=None):
		vendedor = self.get_object(pk)
		serializer = VendedorSerializer(vendedor, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		eventos = Evento.objects.all()
		tieneEventos = False	
		for e in eventos:
			if e.id_producto.id_vendedor.id == pk:
				tieneEventos = True	
		vendedor = self.get_object(pk)
		if tieneEventos:
			vendedor.activo = False
			vendedor.save()
			return Response(status=status.HTTP_200_OK)
		else:
			vendedor.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		

class Categorias_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		categorias = Categoria.objects.all()
		serializer = CategoriaSerializer(categorias, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CategoriaSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriasDetails_APIView(APIView):
	def get_object(self, pk):
		try:
			return Categoria.objects.get(pk=pk)
		except Categoria.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		categoria = self.get_object(pk)
		serializer = CategoriaSerializer(categoria)  
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		categoria = self.get_object(pk)
		serializer = CategoriaSerializer(categoria, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		categoria = self.get_object(pk)
		categoria.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class Eventos_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		eventos = Evento.objects.all()
		serializer = EventoSerializer(eventos, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = EventoSerializer(data=request.data)
		producto = Producto.objects.get(pk=request.data['id_producto'])
		
		if producto.stock - request.data['cantidad'] < 0:
			raise APIException("No puedes realizar esta comprar la cantidad seleccionada supera el stock")
		else:
			if serializer.is_valid():
				serializer.save()
				producto.stock = producto.stock - request.data['cantidad']
				producto.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventosDetails_APIView(APIView):
	def get_object(self, pk):
		try:
			return Evento.objects.get(pk=pk)
		except Evento.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		evento = self.get_object(pk)
		serializer = EventoSerializer(evento)  
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		evento = self.get_object(pk)
		serializer = EventoSerializer(evento, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		evento = self.get_object(pk)
		evento.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ProductosMayoresA_APIView(APIView):
	def get(self, request, pk, format=None):
		productos = Producto.objects.filter(precio__gte=pk)
		serializer = ProductoSerializer(productos, many=True)
		return Response(serializer.data)

class ProductosMenoresA_APIView(APIView):
	def get(self, request, pk, format=None):
		productos = Producto.objects.filter(precio__lte=pk)
		serializer = ProductoSerializer(productos, many=True)
		return Response(serializer.data)

class ProductosEntreRango_APIView(APIView):
	def get(self, request, x1,x2, format=None):
		productos = Producto.objects.filter(precio__gte=x1,precio__lte=x2)
		serializer = ProductoSerializer(productos, many=True)
		return Response(serializer.data)