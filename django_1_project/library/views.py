from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.serializer import BookSerializer, AuthorSerializer

from library.models import Book, Author
# Create your views here.


@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)
    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)

    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)
    if author_serializer.is_valid():
        author_serializer.save()
        return Response(author_serializer.data, status=status.HTTP_201_CREATED)

    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_book_by_id(request, id):
    try:
        book = Book.objects.get(pk=id)
        book_serializer = BookSerializer(book)
        return Response(book_serializer.data, status=status.HTTP_200_OK)

    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def get_author_by_id(request, id):
    try:
        author = Author.objects.get(id=id)
        author_serializer = AuthorSerializer(author)
        return Response(author_serializer.data, status=status.HTTP_200_OK)

    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
