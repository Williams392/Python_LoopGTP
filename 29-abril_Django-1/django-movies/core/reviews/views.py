from .models import Review
from .serializers import ReviewSerializer

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ReviewView(APIView):

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
