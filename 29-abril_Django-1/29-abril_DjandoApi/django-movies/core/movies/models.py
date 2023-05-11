"""
este código es una parte importante para definir el modelo `Movie` 
y sus campos en la base de datos de la aplicación Django.
"""

from django.db import models


# Creando para -> (DJANGO ADMINISTRATION)
class Movie(models.Model):
    name = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()
    synopsis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


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
