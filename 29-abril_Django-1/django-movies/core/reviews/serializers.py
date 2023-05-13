"""
se utiliza para convertir los objetos Movie (definidos en el
modelo) en formato JSON para ser consumidos por una API. El
serializador incluye todos los campos del modelo Movie al
definir 'fields = 'all''.
"""

from rest_framework import serializers

from .models import Review


# 3.1
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'  # Los campos(todos)

        # Todos lo datos de la PELICULA (models.py) -> '__all__'
        # de '__all__' -> uno cada uno ['name', 'year']
