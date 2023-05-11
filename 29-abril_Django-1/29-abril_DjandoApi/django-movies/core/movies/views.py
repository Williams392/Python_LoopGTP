from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


# Create your views here.
def index_movies(request):
    return JsonResponse({'message': 'Online'})


class MovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        # JSON de la PETICION
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({"msg": "Put recibido"})

    def delete(self, request, pk=None):
        return Response({"msg": "Delete recibido"})


# el request es el -> (JSON)
