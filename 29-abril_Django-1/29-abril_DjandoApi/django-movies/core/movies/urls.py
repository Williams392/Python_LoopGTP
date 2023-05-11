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

    path('movie/', MovieView.as_view(), name='movie'),
]
