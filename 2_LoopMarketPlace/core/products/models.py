# (3) models.py

from django.db import models


class Product(models.Model):

    class Meta:
        ordering = ['pk']

    product = models.CharField(max_length=255, unique=True)
    brand = models.CharField(
        max_length=255, unique=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product


'''
1. Actualizar las migraciones y aplicar los cambios:
_ python manage.py makemigrations
_ python manage.py migrate

'''


# 2. Para visualizar en DJANGO administration:
# _ amdmin.py

# . Imágenes en Django:
# _ Error: pipenv install pillow
