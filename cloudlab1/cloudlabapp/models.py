from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    publish_year = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
