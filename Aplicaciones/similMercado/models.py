from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_lenght=30)
    apellido = models.CharField(max_lenght=30)
    email = models.EmailField()

class Vendedores(models.Model):
    razon_social = models.CharField(max_lenght=30)
    email = models.EmailField()

class Productos(models.Model):
    nombre = models.CharField(max_lenght=30)
    descripcion = models.CharField(max_lenght=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    id_vendedor = models.ForeignKey("Vendedores", on_delete=models.CASCADE, blank=False)

class Eventos(models.Model):
    id_usuario_comprador = models.ForeignKey("Usuarios", on_delete=models.RESTRICT, blank=False)
    id_vendedor = models.ForeignKey("Vendedores", on_delete=models.RESTRICT, blank=False)
    id_producto = models.ForeignKey("Productos", on_delete=models.RESTRICT, blank=False)
    fecha_de_compra = models.DateTimeField(auto_now_add=True)