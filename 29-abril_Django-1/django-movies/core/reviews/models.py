from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

# 1. Guardar en (admin.py)
# 2. Esta clase se utiliza para la carpeta -> (serializer.py) -> para la api


# 3.1
class Review(models.Model):

    # pide opcion de nombre del USUARIO -> Django Administration:
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    # Cuando se crea el regitro.
    content = models.TextField()
    # Cuando el objeto se crea.
    created_at = models.DateTimeField(auto_now_add=True)
    # cuando el objeto se actualiza y modifica.
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie.title} - {self.content}"
