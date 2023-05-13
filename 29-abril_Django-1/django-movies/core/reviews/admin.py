from django.contrib import admin

from .models import Review


# 2.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'movie', 'content']


# 1. Registrar (models.py)
admin.site.register(Review,  ReviewAdmin)


# 2. Cuando editamos/crearmos un Modelo que impacte base de datos -> (correr migraciones)

# ---------------------------------------------------------------
#          Comando para base de datos -- (Migraciones)
# ---------------------------------------------------------------

# . Adentro de -> archivo core:

# 1. Genera los archivos de migración para aplicar los cambios en BaseDatos:
# . (Siempre que agamos un cambio esto se debe que HACER para ACTUALIZAR)
# . comando -> [python manage.py makemigrations]

# 2. Aplicar migraciones en el Admin, de todas que trae Django por defecto:
# . comando -> [python manage.py migrate]

# ----------
