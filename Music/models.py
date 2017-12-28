from django.db import models
from django.urls import reverse
from django.urls import reverse


class Genre(models.Model):
    
    # Genre's name
    genre_title = models.CharField(max_length=200)
    # Is favourite genre
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.genre_title
    
    def get_absolute_url(self):
        return reverse('details_genre', kwargs={'pk': self.pk})

class Artist(models.Model):
    
    # Artist's name
    artist = models.CharField(max_length=200)
    # Is favourite artist
    is_favourite = models.BooleanField(default=False)
    # Genres that related to the artist
    related_genres = models.ForeignKey('Genre', on_delete=models.SET('None'), null=True)

    def __str__(self):
        return self.artist

    def get_absolute_url(self):
        return reverse('details_artist', kwargs={'pk': self.pk})

class Album(models.Model):
    
    # Album's title
    album_title = models.CharField(max_length=200)
    # Artist
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, null=True)
    # Genre
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True)
    # Date of release
    realeased = models.DateField(null=True)
    # Is favourite album
    is_favourite = models.BooleanField(default=False)
    # Album cover
    album_cover = models.ImageField(null=True)

    def __str__(self):
        return self.album_title

    def get_absolute_url(self):
        return reverse('details_album', kwargs={'pk': self.pk})

class Song(models.Model):
    
    # Song's title
    song_title = models.CharField(max_length=300)
    # Realeted album
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    # Position in album
    position = models.IntegerField(default=1)
    # Is favourite song
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

