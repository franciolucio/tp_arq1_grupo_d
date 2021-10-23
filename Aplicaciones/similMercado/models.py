from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

class Vendedor(models.Model):
    razon_social = models.CharField(max_length=30)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    id_vendedor = models.ForeignKey("Vendedor", on_delete=models.CASCADE, blank=False)
    nuevo = models.BooleanField()
    id_categoria = models.ForeignKey("Categoria", on_delete=models.RESTRICT, blank=True, null=True)
    activo = models.BooleanField(default=True)

class Evento(models.Model):
    id_usuario_comprador = models.ForeignKey("Usuario", on_delete=models.RESTRICT, blank=False)
    id_producto = models.ForeignKey("Producto", on_delete=models.RESTRICT, blank=False)
    cantidad = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)