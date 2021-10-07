from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from Aplicaciones.similMercado.models import Categoria, Producto,Vendedor
import json

# Create your tests here.

class Productos_APITestCase(TestCase):
      
    def test_get_Productos(self):
        client = APIClient()
        response = client.get(
                '/productos', {}
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_get_specific_Producto(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar',
            activo=True
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        producto = Producto.objects.create(
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            activo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        client = APIClient()
        response = client.get(
            f'/productos/{producto.pk}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, {
                                "nombre": "Gorras",
                                "descripcion": "Para la cancha",
                                "precio": 1000,
                                "stock": 54,
                                "nuevo": True,
                                "activo": True,
                                "id_vendedor": vendedor.id,
                                "id_categoria": categoria.id
                            })
        
    def test_post_Productos(self):
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar',
            activo=True
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        client = APIClient()
        response = client.post(
                '/productos', {
                                "nombre": "Gorras",
                                "descripcion": "Para la cancha",
                                "precio": 1000,
                                "stock": 54,
                                "nuevo": True,
                                "activo": True,
                                "id_vendedor": vendedor.id,
                                "id_categoria": categoria.id
                            },
                format='json'
        )
        result = json.loads(response.content)
        productos = Producto.objects.all()
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(productos.count(), 1)
        self.assertIn('nombre', result)
        self.assertIn('descripcion', result)
        self.assertIn('precio', result)
        self.assertIn('stock', result)
        self.assertIn('nuevo', result)
        self.assertIn('activo', result)
        self.assertIn('id_vendedor', result)
        self.assertIn('id_categoria', result)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, {
                                "nombre": "Gorras",
                                "descripcion": "Para la cancha",
                                "precio": 1000,
                                "stock": 54,
                                "nuevo": True,
                                "activo": True,
                                "id_vendedor": vendedor.id,
                                "id_categoria": categoria.id
                            })
        
    def test_put_Productos(self):
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar',
            activo=True
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        producto = Producto.objects.create(
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            activo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        test_producto_update = {
            "nombre": "Gorras",
            "descripcion": "Para la cancha y la playa",
            "precio": 1000,
            "stock": 54,
            "nuevo": True,
            "activo": True,
            "id_vendedor": vendedor.id,
            "id_categoria": categoria.id
        }
        
        client = APIClient()
        response = client.put(
            f'/productos/{producto.pk}',
            test_producto_update,
            format='json'
        )
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, test_producto_update)
    
    def test_delete_Productos(self):
        client = APIClient()
        
        # Creamos un objeto en la base de datos para trabajar con datos
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar',
            activo=True
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        producto = Producto.objects.create(
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            activo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )

        response = client.delete(
            f'/productos/{producto.pk}', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        edu_exists = Producto.objects.filter(pk=producto.pk)
        self.assertFalse(edu_exists)