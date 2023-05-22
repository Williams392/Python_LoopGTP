# (3) -> actualizar para la importación en el archivo views.py

# serializers.py

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


"""
    Serializer para POST y PUT

    Ejemplo de JSON a enviar en POST / PUT:
        {
            "product": "Leche",
            "price": 3,
            "description": "Me encantó la película"
        }
"""
