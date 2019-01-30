from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'book_name', 'author_name', 'publish_year')


# class StudentViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('id', 'student_name', 'faculty')
