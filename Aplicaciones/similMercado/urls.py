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
  	path('productosDelVendedor/<int:pk>', ProductosAsociadosAlVendedor_APIView.as_view()),
	path('categorias', Categorias_APIView.as_view()),
	path('categorias/<int:pk>', CategoriasDetails_APIView.as_view()),
 	path('eventos', Eventos_APIView.as_view()),
	path('eventos/<int:pk>', EventosDetails_APIView.as_view()),
 	path('productosCompradosPorUsuario/<int:pk>', ProductosCompradoPorUsuario_APIView.as_view()),
  	path('productosVendidosPorVendedor/<int:pk>', ProductosVendidosPorVendedor_APIView.as_view()),
  	path('productosMayorA/<int:pk>', ProductosMayoresA_APIView.as_view()),
   	path('productosMenorA/<int:pk>', ProductosMenoresA_APIView.as_view()),
    path('productosEntre/<int:x1>/<int:x2>', ProductosEntreRango_APIView.as_view()),
    path('cargarProductos/<int:pk>', ProductosCargaMasiva_APIView.as_view()),
]