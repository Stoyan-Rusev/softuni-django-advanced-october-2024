from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from libraryApi.books.models import Book
from libraryApi.books.serializers import BookSerializer


# View without REST Framework(Wrong way to implement the view):
def index(request):
    return JsonResponse({'name': 'Ivan'})


# FBV
@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CBV
class ListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CBV generic view
class ListBooksApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(APIView):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Book, pk=pk)

    @staticmethod
    def serializer_valid(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk: int):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk: int):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book, data=request.data)

        return self.serializer_valid(serializer)

    def patch(self, request, pk: int):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)

        return self.serializer_valid(serializer)

    def delete(self, request, pk: int):
        book = self.get_object(pk=pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)














