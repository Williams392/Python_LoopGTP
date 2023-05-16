"""
Este código es una parte importante para definir 
las rutas y vistas de una aplicación web Django.
"""

from django.contrib import admin
from django.urls import path

from .views import ReviewView


urlpatterns = [
    # path('online/', index_movies, name='index_movies'), # 1_Princial

    path('', ReviewView.as_view(), name='movie'),  # 2_Princial

    path('<int:pk_movie>', ReviewView.as_view(), name='get_review_by_movie'),
    path('review/<int:pk_review>', ReviewView.as_view(),
         name='update_and_delete_review'),
]


# Apuntes:
# La función path crea una ruta -> URL relativa a la raíz del sitio web.
# -------------------------------
# Los 2 apuntas al mismo Lugar:
# _ (int:pk) se utiliza para capturar un valor numérico de la URL
# _ (`pk`): se refiere a la clave primaria de la instancia de la película que se está solicitando
# -------------------------------
