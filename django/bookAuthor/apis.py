from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Author, Book, BookAuthor
from .serializers import BookSerializer

# Retrieve books written by a specific author (e.g., Author 1)
class GetBookByAuthor(APIView):

    def get(self, request):
        queryset = Book.objects.filter(authors__name='Author 1')
        serializer = BookSerializer(queryset, many=True)

        return Response(serializer.data)