"""
Este código es una parte importante para definir 
las rutas y vistas de una aplicación web Django.
"""

from django.contrib import admin
from django.urls import path

from .views import index_movies, MovieView

# La función path crea una ruta -> URL relativa a la raíz del sitio web.
urlpatterns = [
    path('online/', index_movies, name='index_movies'),

    path('', MovieView.as_view(), name='movie'), # Princial
    path('<int:pk>', MovieView.as_view(), name='one_movie'),
]



# Apuntes:
# 1. ('movie/',) -> dejango vacio
# ------
# Los 2 apuntas al mismo Lugar:
# _ (int:pk) se utiliza para capturar un valor numérico de la URL
# _ `pk`: se refiere a la clave primaria de la instancia de la película que se está solicitando
# ------