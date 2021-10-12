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
    tipoCategoria = serializers.CharField(source='id_producto.id_categoria.nombre',required=False)
    nombreVendedor = serializers.CharField(source='id_producto.id_vendedor.razon_social',required=False)
    nombreCompletoComprador = serializers.SerializerMethodField(required=False)
    fechaDeCompra = serializers.DateField(source='fecha_de_compra',format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'],required=False)
    def get_nombreCompletoComprador(self, obj):
        return '{} {}'.format(obj.id_usuario_comprador.nombre, obj.id_usuario_comprador.apellido) 
    class Meta:
        model = Evento
        fields = ['id','id_producto', 'id_usuario_comprador', 'tipoCategoria','nombreVendedor','cantidad','nombreCompletoComprador','fechaDeCompra']
