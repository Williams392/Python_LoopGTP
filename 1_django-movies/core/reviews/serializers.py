"""
se utiliza para convertir los objetos Movie (definidos en el
modelo) en formato JSON para ser consumidos por una API. El
serializador incluye todos los campos del modelo Movie al
definir 'fields = 'all''.
"""

from rest_framework import serializers

from .models import Review
# 3.2 (models.py)


# Operacion NORMAL:
class ReviewSerializer(serializers.ModelSerializer):

    # Serializer para POST y PUT

    class Meta:
        model = Review
        fields = '__all__'


# Operacion MAS AVANZADO:
class ReviewDetailSerializer(serializers.ModelSerializer):

    # Serializer para GET (Listar detalles)

    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'      # (todos) Los campos
        depth = 1               # Envia los datos del Usuario


# APUNTES:
# Todos lo datos de la PELICULA (models.py) -> '__all__'
# de '__all__' -> uno cada uno ['name', 'year']
