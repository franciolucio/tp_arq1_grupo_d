from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from Aplicaciones.similMercado.models import Categoria,Producto,Vendedor,Usuario,Evento
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
            email='jumbo@hotmail.com.ar'
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
                                "id_vendedor": vendedor.id,
                                "id_categoria": categoria.id,
                                "tipo_categoria": "Indumentaria",
                                "nombre_vendedor": "JUMBO"
                            })
        
    def test_get_ProductosConStock(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        Producto.objects.create(
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        client = APIClient()
        response = client.get(
            '/productosConStock', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(result),1)
    
    def test_get_ProductosAsociadosAlVendedor(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        Producto.objects.create(
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        client = APIClient()
        response = client.get(
            f'/productosDelVendedor/{vendedor.pk}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(result),1)
        
    def test_get_ProductosMayorA(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        Producto.objects.create(
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        client = APIClient()
        response = client.get(
            f'/productosMayorA/{900}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(result),1)
        
    def test_get_ProductosMenorA(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        Producto.objects.create(
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        client = APIClient()
        response = client.get(
            f'/productosMenorA/{1200}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(result),1)
        
    def test_get_ProductosEntre(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )
        
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        Producto.objects.create(
            nombre='Gorras',
            descripcion = 'Para la cancha',
            precio = 1000,
            stock = 54,
            nuevo = True,
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        client = APIClient()
        response = client.get(
            f'/productosEntre/{900}/{1200}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(result),1)
        
    def test_get_ProductosCompradosPorUsuarios(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        
        usuario = Usuario.objects.create(
            nombre='Javier',
            apellido='Pastore',
            email='pastore@gmail.com.ar',
        )
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
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
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        Evento.objects.create(
            id_usuario_comprador = usuario,
            id_producto = producto,
            cantidad = 2
        )
        
        client = APIClient()
        response = client.get(
            f'/productosCompradosPorUsuario/{usuario.pk}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(result),1)
        
    def test_get_ProductosVendidosPorVendedor(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        
        usuario = Usuario.objects.create(
            nombre='Javier',
            apellido='Pastore',
            email='pastore@gmail.com.ar'
        )
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
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
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        Evento.objects.create(
            id_usuario_comprador = usuario,
            id_producto = producto,
            cantidad = 2
        )
        
        client = APIClient()
        response = client.get(
            f'/productosVendidosPorVendedor/{vendedor.pk}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(result),1)
        
    def test_post_Productos(self):
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
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
                                "id_vendedor": vendedor.id,
                                "id_categoria": categoria.id,
                                "tipo_categoria": "Indumentaria",
                                "nombre_vendedor": "JUMBO"
                            })
        
    def test_put_Productos(self):
        
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
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
            id_vendedor = vendedor,
            id_categoria = categoria,
        )
        
        test_producto_update = {
            "nombre": "Gorras",
            "descripcion": "Para la cancha y la playa",
            "precio": 1000,
            "stock": 54,
            "nuevo": True,
            "id_vendedor": vendedor.id,
            "id_categoria": categoria.id,
            "tipo_categoria": "Indumentaria",
            "nombre_vendedor": "JUMBO"
        }
        
        client = APIClient()
        response = client.put(
            f'/productos/{producto.pk}',
            {
            "nombre": "Gorras",
            "descripcion": "Para la cancha y la playa",
            "precio": 1000,
            "stock": 54,
            "nuevo": True,
            "id_vendedor": vendedor.id,
            "id_categoria": categoria.id
            },
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
            email='jumbo@hotmail.com.ar'
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