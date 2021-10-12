from rest_framework import serializers
from Aplicaciones.similMercado.models import Usuario,Producto,Categoria,Vendedor,Evento


# Serializers define the API representation.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields ='__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields ='__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields ='__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    tipo_categoria = serializers.CharField(source='id_categoria.nombre',required=False)
    nombre_vendedor = serializers.CharField(source='id_vendedor.razon_social',required=False)
    class Meta:
        model = Producto
        fields =['id','id_vendedor','id_categoria','nombre','descripcion','precio','stock','nuevo','tipo_categoria','nombre_vendedor']
        
class EventoSerializer(serializers.ModelSerializer):
    tipo_categoria = serializers.CharField(source='id_producto.id_categoria.nombre',required=False)
    nombre_vendedor = serializers.CharField(source='id_producto.id_vendedor.razon_social',required=False)
    nombre_comprador = serializers.CharField(source='id_usuario_comprador.nombre',required=False)
    apellido_comprador = serializers.CharField(source='id_usuario_comprador.apellido',required=False)
    class Meta:
        model = Evento
        fields = ['id','id_producto', 'id_usuario_comprador', 'tipo_categoria','nombre_vendedor','cantidad','nombre_comprador','apellido_comprador','fecha_de_compra']