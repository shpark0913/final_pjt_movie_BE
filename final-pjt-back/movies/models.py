from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    genreid = models.IntegerField(primary_key=True)
    name = models.TextField()

class Movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    vote_average = models.BooleanField()
