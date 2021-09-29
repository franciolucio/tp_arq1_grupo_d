from rest_framework import serializers
from Aplicaciones.similMercado.models import Usuario,Producto,Categoria,Vendedor,Evento


# Serializers define the API representation.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields ='__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields ='__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields ='__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields ='__all__'
        
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields ='__all__'