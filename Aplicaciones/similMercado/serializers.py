from rest_framework import serializers
from Aplicaciones.similMercado.models import Usuario


# Serializers define the API representation.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','email']