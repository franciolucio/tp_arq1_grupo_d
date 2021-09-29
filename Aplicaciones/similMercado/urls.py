from django.urls import path
from .views import *

urlpatterns = [
	path('', index),
	path('usuarios', Usuarios_APIView.as_view()),
	path('usuarios/<int:pk>', UsuariosDetails_APIView.as_view()),
 	path('vendedores', Vendedores_APIView.as_view()),
  	path('vendedores/<int:pk>', VendedoresDetails_APIView.as_view()),
	path('productos', Productos_APIView.as_view()),
	path('productos/<int:pk>', ProductosDetails_APIView.as_view()),
 	path('productosConStock', ProductosConStock_APIView.as_view()),
  	path('productosDelVendedor/<int:pk>', ProductosAsociadosAlCliente_APIView.as_view()),
	path('categorias', Categorias_APIView.as_view()),
	path('categorias/<int:pk>', CategoriasDetails_APIView.as_view()),
 	path('eventos', Eventos_APIView.as_view()),
	path('eventos/<int:pk>', EventosDetails_APIView.as_view()),
 	path('productosUsuario/<int:pk>', ProductosUsuarios_APIView.as_view()),
]