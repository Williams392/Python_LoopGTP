# CREADA, no viene incluida:

from datetime import datetime

from django.shortcuts import render

from django.contrib.auth import authenticate  # 5

from rest_framework.views import APIView  # 1
from rest_framework.response import Response  # 2
from rest_framework import status  # 3

from .serializers import LoginSerializer, UserSerializer  # 4


# Se utiliza para autenticar a los usuarios utilizando las credenciales proporcionadas.
class LoginView(APIView):

    # Obtuvimos el tipo USUARIO
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        print(user)

        # Si no es NONE, Significa que el usuario existe y tiene credenciales válidas:
        if user is not None:
            user.last_login = datetime.now()
            user.save()
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "error": "401 Unauthorized",
                    "message": "The credentiales provided are not valid. Please review your information and try again."
                },
                status=status.HTTP_401_UNAUTHORIZED)


# Se utiliza para registrar nuevos usuarios en el sistema.
class SignUpView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:     # Si :)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:  # No se logro guardar el objeto :(
            return Response(
                {
                    "error": "400 Bad Request",
                    "message": f"Email '{serializer.validated_data['email']}' is already registered"
                },
                status=status.HTTP_400_BAD_REQUEST)
