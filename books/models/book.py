from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    FORMAT_CHOICES = [
        ('PHYSICAL', 'Physical'),
        ('EBOOK', 'Ebook'),
        ('AUDIOBOOK', 'Audiobook'),
    ]

    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    language = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_date = models.DateField(null=True, blank=True)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default='PHYSICAL')

    authors = models.ManyToManyField(Author, through='BookAuthor', related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title