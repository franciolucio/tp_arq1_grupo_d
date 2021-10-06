from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from Aplicaciones.similMercado.models import Usuario
import json

# Create your tests here.

class Usuarios_APITestCase(TestCase):
    
    def setUp(self):
        usuario = Usuario(
            nombre='Test',
            apellido='Case',
            email='testcase@gmail.com',
            activo=True
        )
        usuario.save()
        
    def test_get_Usuarios(self):
        client = APIClient()
        response = client.get(
                '/usuarios', {}
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_post_Usuarios(self):
        client = APIClient()
        response = client.post(
                '/usuarios', {
                                "nombre": "Javier",
                                "apellido": "Pastore",
                                "email": "pastore@gmail.com.ar",
                                "activo": True
                            },
                format='json'
        )
        result = json.loads(response.content)
        usuarios = Usuario.objects.all()
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(usuarios.count(), 2)
        self.assertIn('nombre', result)
        self.assertIn('apellido', result)
        self.assertIn('email', result)
        self.assertIn('activo', result)