from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from Aplicaciones.similMercado.models import Vendedor
import json

# Create your tests here.

class Vendedores_APITestCase(TestCase):
      
    def test_get_Vendedores(self):
        client = APIClient()
        response = client.get(
                '/vendedores', {}
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_get_specific_Vendedor(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )
        
        client = APIClient()
        response = client.get(
            f'/vendedores/{vendedor.pk}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, {
                                "razon_social": "JUMBO",
                                "email": "jumbo@hotmail.com.ar"
                            })
        
    def test_post_Vendedores(self):
        client = APIClient()
        response = client.post(
                '/vendedores', {
                                "razon_social": "JUMBO",
                                "email": "jumbo@hotmail.com.ar"
                            },
                format='json'
        )
        result = json.loads(response.content)
        vendedores = Vendedor.objects.all()
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(vendedores.count(), 1)
        self.assertIn('razon_social', result)
        self.assertIn('email', result)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, {
                                "razon_social": "JUMBO",
                                "email": "jumbo@hotmail.com.ar"
                            })
        
    def test_put_Vendedores(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )
        
        test_vendedor_update = {
           "razon_social": "JUMBO",
            "email": "jumbo@hotmail.com.ar"
        }
        
        client = APIClient()
        response = client.put(
            f'/vendedores/{vendedor.pk}',
            test_vendedor_update,
            format='json'
        )
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, test_vendedor_update)
    
    def test_delete_Vendedores(self):
        client = APIClient()
        
        # Creamos un objeto en la base de datos para trabajar con datos
        vendedor = Vendedor.objects.create(
            razon_social='JUMBO',
            email='jumbo@hotmail.com.ar'
        )

        response = client.delete(
            f'/vendedores/{vendedor.pk}', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        edu_exists = Vendedor.objects.filter(pk=vendedor.pk)
        self.assertFalse(edu_exists)