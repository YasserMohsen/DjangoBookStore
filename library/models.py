from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import os
import time

def book_upload_path(instance, filename):
    return os.path.join('static/images/books/', str(int(time.time())) + "_" + filename)
def author_upload_path(instance, filename):
    return os.path.join('static/images/authors/', str(int(time.time())) + "_" + filename)

class Book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    published_at = models.DateField()
    summary = models.TextField(max_length=10000, blank=True)
    country = models.CharField(max_length=50, default='Egypt')
    link = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=20, default='English')
    pages = models.IntegerField()
    cover = models.ImageField(upload_to=book_upload_path)
    author_id = models.ForeignKey('Author', on_delete = models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete = models.CASCADE)
    users = models.ManyToManyField(User, through='User_Book')

    def _get_rating(self):
        rating = User_Book.objects.filter(book_id=self.id).aggregate(avg_rating=models.Avg('rating'))
        return rating['avg_rating'] or 0.0

    rating = property(_get_rating)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    born_at = models.DateField()
    died_at = models.DateField(null=True,blank=True)
    contact = models.CharField(max_length=100)
    about = models.TextField(max_length=10000,blank=True)
    profile = models.ImageField(upload_to=author_upload_path)
    users = models.ManyToManyField(User, through='User_Author')

    def _get_rating(self):
        rating = User_Author.objects.filter(author_id=self.id).aggregate(avg_rating=models.Avg('rating'))
        return rating['avg_rating'] or 0.0

    rating = property(_get_rating)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class User_Book(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=(
        ('r', 'read'),
        ('t', 'to be read'),
        ('c', 'currently reading'),
        ('n', 'nothing')
    ), default='n')
    rating = models.FloatField(default=0.0,
       validators=[
           MaxValueValidator(5.0),
           MinValueValidator(0.0)
       ])

class User_Author(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE)
    follow = models.BooleanField(default=0)
    rating = models.FloatField(default=0.0,
       validators=[
           MaxValueValidator(5.0),
           MinValueValidator(0.0)
       ])