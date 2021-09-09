from django.urls import path

from Aplicaciones.similMercado import views

urlpatterns = [
    path('', views.home, name="Home"),
]