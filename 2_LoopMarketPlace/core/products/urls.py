# (2) urls.py

from django.urls import path
from .views import ProtectedView, ProductListView, ProductDetailView


urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
