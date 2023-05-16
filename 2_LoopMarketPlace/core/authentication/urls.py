# CREADA, no viene incluida:

from django.urls import path  # 1
from .views import LoginView, SignUpView  # 2

from rest_framework.authtoken.views import obtain_auth_token  # 3

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('get-api-token/', obtain_auth_token)
]
