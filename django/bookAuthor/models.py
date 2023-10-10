from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, through='BookAuthor')

    def __str__(self):
        return self.title

class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.author.name} - {self.book.title} ({self.publication_date})"
