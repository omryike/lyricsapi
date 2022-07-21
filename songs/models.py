from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=200)
    lyrics = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    