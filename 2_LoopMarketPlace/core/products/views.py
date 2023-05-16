from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Desde la otra carpeta, para validar y deserializar los datos del usuario:
from authentication.serializers import UserSerializer


class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication]

    # Valida si el usuario se encuentra validado(si inicio seccion).
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(
            serializer.data
        )


""""
Paso 5:

. Creando una vista PROTEGIDA:
  _ Para solo mostrar al dueño del proveerdor, el desorrollador, etc.
    . Para ver la lista de ventas, etc.

"""
