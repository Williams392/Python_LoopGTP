from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index_movies(request):
    return JsonResponse({'message': 'Online'})
