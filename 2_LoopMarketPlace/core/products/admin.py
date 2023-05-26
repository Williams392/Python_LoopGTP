# 4

from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'price', 'description', 'image')
    ordering = ('-id',)


admin.site.register(Product, ProductAdmin)


# Para visualizal todos los dantos en el Django administration
'''
. search_fields = campos_de_búsqueda
. list_display = mostrar_lista
. list_filter  = lista_filtro
'''
