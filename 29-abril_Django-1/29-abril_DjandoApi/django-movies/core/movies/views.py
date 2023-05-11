from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def index_movies(request):
    return JsonResponse({'message': 'Online'})


class MovieView(APIView):
    def get(self, request, pk=None):
        return Response({"msg": "Get recibido"}, )
