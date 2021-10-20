from rest_framework import serializers
from Aplicaciones.similMercado.models import Usuario,Producto,Categoria,Vendedor,Evento


# Serializers define the API representation.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','nombre','apellido','email']

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields =  ['id','razon_social','email']

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
    fecha_compra = serializers.DateTimeField(source='created',format="%d-%m-%Y %H:%M", input_formats=['%d-%m-%Y %H:%M', 'iso-8601'],required=False)
    
    def get_usuario_comprador(self, obj):
        return '{} {}'.format(obj.id_usuario_comprador.nombre, obj.id_usuario_comprador.apellido) 
    class Meta:
        model = Evento
        fields = ['id','id_producto', 'id_usuario_comprador', 'precio','nombre','descripcion','nuevo','tipo_categoria','nombre_vendedor','cantidad','usuario_comprador','fecha_compra']
