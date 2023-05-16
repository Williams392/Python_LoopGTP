""""
.Primer paso:

1. Registrar el settings en core ('products',).
2. agregar la urls en la principal carpeta (core):
   _ ath('products/', include('products.urls')),
   
3. crear el archivo (urls.py) en la carpeta "products"
4. Crear la (urls) en dentro del archivo "urls.py".  
5. el paso 5 esta en el (views.py)

"""


from django.urls import path
from .views import ProtectedView

urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected')

]
