"""
Este código es una parte importante para registrar y personalizar la 
presentación del modelo `Movie` en el panel de administración de Django.
"""

from django.contrib import admin
from .models import Movie


# de carpeta -> MODELS cleando:
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year']
    list_filter = ['year']


# Register your models here.
admin.site.register(Movie, MovieAdmin)


# ---------------------------------------------------------------
# Siempre para cada modificacion y Creando cossas nuevas en DJANGO
# ---------------------------------------------------------------
# Adentro de -> archivo core:

# 1. Genera los archivos de migración para los cambios en BaseDatos:
# (Siempre que agamos un cambio esto se debe que HACER para ACTUALIZAR)
# comando -> [python manage.py makemigrations]

# 2. Aplicar migraciones en el Admin, de todas que trae Django por defecto:
# _ comando -> [python manage.py migrate]

# ---------------------------------------------------------------
