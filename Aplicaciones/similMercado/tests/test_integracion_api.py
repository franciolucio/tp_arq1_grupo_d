from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from Aplicaciones.similMercado.models import Evento,Usuario,Producto,Vendedor,Categoria
import json

# Create your tests here.

class Integration_APITestCase(TestCase):
    
    
    def test_realizar_compra(self):
        
        client = APIClient()
        client.post(
                    '/usuarios', {
                                "nombre": "Javier",
                                "apellido": "Pastore",
                                "email": "pastore@gmail.com.ar"
                            },
                    format='json'
                )
        usuario = Usuario.objects.all().first()
        client.post(
                    '/vendedores', {
                                    "razon_social": "JUMBO",
                                    "email": "jumbo@hotmail.com.ar"
                                },
                    format='json'
                )
        vendedor = Vendedor.objects.all().first()
        client.post(
                    '/categorias', {
                                "nombre": "Indumentaria"
                                },
                    format='json'
                )
        categoria = Categoria.objects.all().first()
        client.post(
                    '/productos', {
                                    "nombre": "Gorras",
                                    "descripcion": "Para la cancha",
                                    "precio": 1000,
                                    "stock": 54,
                                    "nuevo": True,
                                    "id_vendedor": vendedor.id,
                                    "id_categoria": categoria.id
                                },
                    format='json'
                )
        producto = Producto.objects.all().first()
        creacionCompra = client.post(
                                '/eventos', {
                                            "id_usuario_comprador": usuario.id,
                                            "id_producto": producto.id,
                                            "cantidad": 2
                                            },
                                format='json'
                            )
        resultCreacionCompra = json.loads(creacionCompra.content)
        eventos = Evento.objects.all()
        self.assertEqual(creacionCompra.status_code,status.HTTP_201_CREATED)
        self.assertEqual(eventos.count(), 1)
        self.assertIn('id_usuario_comprador', resultCreacionCompra)
        self.assertIn('id_producto', resultCreacionCompra)
        self.assertIn('cantidad', resultCreacionCompra)