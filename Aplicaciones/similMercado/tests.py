from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import Usuario
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
        response = client.post(
                '/usuarios', {}
        )
        self.assertEqual(json.loads(response.content), {"nombre": "Test","apellido": "Case","email": "testcase@gmail.com","activo": True})