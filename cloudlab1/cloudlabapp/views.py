from rest_framework import viewsets
from django.shortcuts import render
from .models import Book
from .serializer import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('book_name', 'author_name', 'publish_year')

    # def get_queryset(self):
    #     queryset = Student.objects.all()
    #     username = self.request.query_params.get('id', None)
    #     if username is not None:
    #         queryset = queryset.filter(id=username)
    #     return queryset
