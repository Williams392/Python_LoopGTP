# CREADA, no viene incluida:

from django.urls import path  # 1
from .views import LoginView, SignUpView  # 2

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
