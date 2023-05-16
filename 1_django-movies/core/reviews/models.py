"""
Para registrar los MODELOS, una especia de tabla para e DJANGO ADMINISTRATION.
"""

from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

# 1. Guardar en (admin.py)
# 2. Esta clase se utiliza para la carpeta -> (serializer.py) -> para la api


# 3.1 (serializer.py)
class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie.title} - {self.content}"


# Apuntes:
# ( user = ) pide opcion de nombre del USUARIO -> Django Administration.
# ( content = ) Cuando se crea el regitro.
# ( created_at = ) Cuando el objeto se crea.
# ( last_updated = )cuando el objeto se actualiza y modifica
