from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Book, Author, BookAuthor


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ("id", "name")