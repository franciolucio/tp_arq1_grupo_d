from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from Aplicaciones.similMercado.models import Usuario
import json

# Create your tests here.

class Usuarios_APITestCase(TestCase):
      
    def test_get_Usuarios(self):
        client = APIClient()
        response = client.get(
                '/usuarios', {}
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_get_specific_Usuario(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        usuario = Usuario.objects.create(
            nombre='Javier',
            apellido='Pastore',
            email='pastore@gmail.com.ar'
        )
        
        client = APIClient()
        response = client.get(
            f'/usuarios/{usuario.pk}', {},
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, {
                                "nombre": "Javier",
                                "apellido": "Pastore",
                                "email": "pastore@gmail.com.ar"
                            })
        
    def test_post_Usuarios(self):
        client = APIClient()
        response = client.post(
                '/usuarios', {
                                "nombre": "Javier",
                                "apellido": "Pastore",
                                "email": "pastore@gmail.com.ar"
                            },
                format='json'
        )
        result = json.loads(response.content)
        usuarios = Usuario.objects.all()
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(usuarios.count(), 1)
        self.assertIn('nombre', result)
        self.assertIn('apellido', result)
        self.assertIn('email', result)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, {
                                "nombre": "Javier",
                                "apellido": "Pastore",
                                "email": "pastore@gmail.com.ar"
                            })
        
    def test_put_Usuarios(self):
        
        # Creamos un objeto en la base de datos para trabajar con datos
        usuario = Usuario.objects.create(
            nombre='Javier',
            apellido='Pastore',
            email='pastore@gmail.com.ar'
        )
        
        test_usuario_update = {
            'nombre': 'Javier',
            'apellido': 'Pastore',
            'email': 'pastore@hotmail.com'
        }
        
        client = APIClient()
        response = client.put(
            f'/usuarios/{usuario.pk}',
            test_usuario_update,
            format='json'
        )
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if 'id' in result:
            del result['id']
            
        self.assertEqual(result, test_usuario_update)
    
    def test_delete_Usuarios(self):
        client = APIClient()
        
        # Creamos un objeto en la base de datos para trabajar con datos
        usuario = Usuario.objects.create(
            nombre='Javier',
            apellido='Pastore',
            email='pastore@gmail.com.ar'
        )

        response = client.delete(
            f'/usuarios/{usuario.pk}', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        edu_exists = Usuario.objects.filter(pk=usuario.pk)
        self.assertFalse(edu_exists)