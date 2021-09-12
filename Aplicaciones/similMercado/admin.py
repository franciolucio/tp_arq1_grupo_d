from django.contrib import admin

from Aplicaciones.similMercado.models import Usuario,Producto,Categoria,Evento,Vendedor

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Evento)
admin.site.register(Vendedor)