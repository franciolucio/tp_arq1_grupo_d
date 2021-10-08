from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from Aplicaciones.similMercado.models import Categoria
import json

# Create your tests here.

class Categorias_APITestCase(TestCase):
      
    def test_get_Categorias(self):
        client = APIClient()
        response = client.get(
                '/categorias', {}
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_get_specific_Categoria(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        client = APIClient()
        response = client.get(
            f'/categorias/{categoria.pk}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, {
                                "nombre": "Indumentaria"
                            })
        
    def test_post_Categorias(self):
        client = APIClient()
        response = client.post(
                '/categorias', {
                               "nombre": "Indumentaria"
                            },
                format='json'
        )
        result = json.loads(response.content)
        categorias = Categoria.objects.all()
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(categorias.count(), 1)
        self.assertIn('nombre', result)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, {
                                "nombre": "Indumentaria"
                            })
        
    def test_put_Categorias(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )
        
        test_categoria_update = {
            'nombre': 'Calzado'
        }
        
        client = APIClient()
        response = client.put(
            f'/categorias/{categoria.pk}',
            test_categoria_update,
            format='json'
        )
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, test_categoria_update)
    
    def test_delete_Categorias(self):
        client = APIClient()
        
        # Creamos un objeto en la base de datos para trabajar con datos
        categoria = Categoria.objects.create(
            nombre='Indumentaria'
        )

        response = client.delete(
            f'/categorias/{categoria.pk}', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        edu_exists = Categoria.objects.filter(pk=categoria.pk)
        self.assertFalse(edu_exists)