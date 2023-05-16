from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer

from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class ReviewView(APIView):

    def get(self, request, pk_movie=None, pk_review=None):
        if pk_movie:  # ver cada ID
            reviews = Review.objects.filter(movie=pk_movie)
        else:         # ver todo
            reviews = Review.objects.all()

        serializer = ReviewDetailSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk_review=None, pk_movie=None):
        print(pk_review)
        review = get_object_or_404(Review, pk=pk_review)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_review = None):
        if pk_review:
            review = get_object_or_404(Review, pk = pk_review)
            review.delete()
        else:
            return Response(
                {"msg":"Necesitas enviar el ID de la review a eliminar"}, 
                status = status.HTTP_400_BAD_REQUEST
            )
        return Response({"msg": f"Reseña con ID {pk_review} ha sido eliminada"})


# Tarea:
# [get =]Aplicar el filtro por usuario(tarea)
