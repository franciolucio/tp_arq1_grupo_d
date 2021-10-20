from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from Aplicaciones.similMercado.models import Evento,Usuario,Producto,Vendedor,Categoria
import json

# Create your tests here.

class Eventos_APITestCase(TestCase):
    
    def setUp(self):
        
        vendedor = Vendedor.objects.create(
            activo = True,
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        Usuario.objects.create(
            activo = True,
            nombre='Javier',
            apellido='Pastore',
            email='pastore@gmail.com.ar'
        )
        
        Producto.objects.create(
            activo = True,
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
    def test_get_Eventos(self):
        client = APIClient()
        response = client.get(
                '/eventos', {}
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_get_specific_Evento(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        comprador = Usuario.objects.all().first()
        producto = Producto.objects.all().first()
        evento = Evento.objects.create(
            id_usuario_comprador = comprador,
            id_producto = producto,
            cantidad = 2
        )
        
        client = APIClient()
        response = client.get(
            f'/eventos/{evento.pk}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            del result['fecha_compra']
            
        self.assertEqual(result, {
                                "id_usuario_comprador": comprador.id,
                                "id_producto": producto.id,
                                "cantidad": 2,
                                "tipo_categoria": "Indumentaria",
                                "nombre_vendedor": "JUMBO",
                                "usuario_comprador": "Javier Pastore",
                                "precio" : 1000,
                                "nombre" : "Gorras",
                                "descripcion" : "Para la cancha",
                                "nuevo" : True
                            })
        
    def test_post_Eventos(self):
        comprador = Usuario.objects.all().first()
        producto = Producto.objects.all().first()
        client = APIClient()
        response = client.post(
                '/eventos', {
                            "id_usuario_comprador": comprador.id,
                            "id_producto": producto.id,
                            "cantidad": 2
                            },
                format='json'
        )
        result = json.loads(response.content)
        eventos = Evento.objects.all()
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(eventos.count(), 1)
        self.assertIn('id_usuario_comprador', result)
        self.assertIn('id_producto', result)
        self.assertIn('cantidad', result)
        
        if 'id' in result:
            del result['id']
            del result['fecha_compra']
            
        self.assertEqual(result, {
                                "id_usuario_comprador": comprador.id,
                                "id_producto":  producto.id,
                                "cantidad": 2,
                                "tipo_categoria": "Indumentaria",
                                "nombre_vendedor": "JUMBO",
                                "usuario_comprador": "Javier Pastore",
                                "precio" : 1000,
                                "nombre" : "Gorras",
                                "descripcion" : "Para la cancha",
                                "nuevo" : True
                            })
        
    def test_put_Eventos(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        producto = Producto.objects.all().first()
        comprador = Usuario.objects.all().first()
        evento = Evento.objects.create(
            id_usuario_comprador = comprador,
            id_producto = producto,
            cantidad = 2
        )
        
        test_evento_update = {
            "id_usuario_comprador": comprador.id,
            "id_producto": producto.id,
            "cantidad": 6,
            "tipo_categoria": "Indumentaria",
            "nombre_vendedor": "JUMBO",
            "usuario_comprador": "Javier Pastore",
            "precio" : 1000,
            "nombre" : "Gorras",
            "descripcion" : "Para la cancha",
            "nuevo" : True
        }
        
        client = APIClient()
        response = client.put(
            f'/eventos/{evento.pk}',
            {
                "id_usuario_comprador": comprador.id,
                "id_producto": producto.id,
                "cantidad": 6
            },
            format='json'
        )
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            del result['fecha_compra']
            
        self.assertEqual(result, test_evento_update)
    
    def test_delete_Eventos(self):
        client = APIClient()
        
        # Creamos un objeto en la base de datos para trabajar con datos
        comprador = Usuario.objects.all().first()
        producto = Producto.objects.all().first()
        evento = Evento.objects.create(
            id_usuario_comprador = comprador,
            id_producto = producto,
            cantidad = 2
        )

        response = client.delete(
            f'/eventos/{evento.pk}', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        edu_exists = Evento.objects.filter(pk=evento.pk)
        self.assertFalse(edu_exists)