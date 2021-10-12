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
    tipoCategoria = serializers.CharField(source='id_categoria.nombre',required=False)
    nombreVendedor = serializers.CharField(source='id_vendedor.razon_social',required=False)
    class Meta:
        model = Producto
        fields =['id','id_vendedor','id_categoria','nombre','descripcion','precio','stock','nuevo','tipoCategoria','nombreVendedor']
        
class EventoSerializer(serializers.ModelSerializer):
    tipoCategoria = serializers.CharField(source='id_producto.id_categoria.nombre',required=False)
    nombreVendedor = serializers.CharField(source='id_producto.id_vendedor.razon_social',required=False)
    nombreComprador = serializers.CharField(source='id_usuario_comprador.nombre',required=False)
    apellidoComprador = serializers.CharField(source='id_usuario_comprador.apellido',required=False)
    class Meta:
        model = Evento
        fields = ['id','id_producto', 'id_usuario_comprador', 'tipoCategoria','nombreVendedor','cantidad','nombreComprador','apellidoComprador','fecha_de_compra']