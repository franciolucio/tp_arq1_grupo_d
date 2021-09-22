from django.urls import path
from Aplicaciones.similMercado import views

urlpatterns = [
	path('', views.index, name="api-overview"),
	path('usuarios-get', views.usuariosList, name="usuario-list"),
	path('usuarios-get/<str:pk>', views.usuariosDetail, name="usuario-detail"),
    path('usuarios-post', views.usuarioCreate, name="usuario-create"),
	path('usuarios-post/<str:pk>', views.usuarioUpdate, name="usuario-update"),
	path('usuarios-delete/<str:pk>', views.usuarioDelete, name="usuario-delete"),
	path('productos-get', views.productosList, name="productos-list"),
	path('productos-get/<str:pk>', views.productosDetail, name="productos-detail"),
    path('productos-post', views.productosCreate, name="productos-create"),
	path('productos-post/<str:pk>', views.productosUpdate, name="productos-update"),
	path('productos-delete/<str:pk>', views.productosDelete, name="productos-delete"),
    path('vendedores-get', views.vendedoresList, name="vendedores-list"),
	path('vendedores-get/<str:pk>', views.vendedoresDetail, name="vendedores-detail"),
    path('vendedores-post', views.vendedoresCreate, name="vendedores-create"),
	path('vendedores-post/<str:pk>', views.vendedoresUpdate, name="vendedores-update"),
	path('vendedores-delete/<str:pk>', views.vendedoresDelete, name="vendedores-delete"),
]