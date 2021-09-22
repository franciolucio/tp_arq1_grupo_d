from django.conf.urls import url
from Aplicaciones.similMercado import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^usuarios$',views.usuarioApi),
    url(r'^usuarios/([0-9]+)$',views.usuarioApi)
]