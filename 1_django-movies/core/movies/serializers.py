"""
se utiliza para convertir los objetos Movie (definidos en el
modelo) en formato JSON para ser consumidos por una API. El
serializador incluye todos los campos del modelo Movie al
definir 'fields = 'all''.
"""

from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

        # Todos lo datos de la PELICULA (models.py) -> '__all__'
        # de '__all__' -> uno cada uno ['name', 'year']
