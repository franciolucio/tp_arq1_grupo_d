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
    precio = serializers.IntegerField(source='id_producto.precio',required=False)
    nombre = serializers.CharField(source='id_producto.nombre',required=False)
    descripcion = serializers.CharField(source='id_producto.descripcion',required=False)
    nuevo = serializers.BooleanField(source='id_producto.nuevo',required=False)
    nombre_vendedor = serializers.CharField(source='id_producto.id_vendedor.razon_social',required=False)
    usuario_comprador = serializers.SerializerMethodField(required=False)
    fecha_compra = serializers.DateField(source='fecha_de_compra',format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'],required=False)
    
    def get_usuario_comprador(self, obj):
        return '{} {}'.format(obj.id_usuario_comprador.nombre, obj.id_usuario_comprador.apellido) 
    class Meta:
        model = Evento
        fields = ['id','id_producto', 'id_usuario_comprador', 'tipo_categoria','nombre_vendedor','cantidad','usuario_comprador','fecha_compra']
