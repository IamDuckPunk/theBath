from django import forms
#from django.contrib.auth.models import User

from . import models


class ArtistForm(forms.ModelForm):

    class Meta:
        model = models.Artist
        fields = ['artist']


class GenreForm(forms.ModelForm):

    class Meta:
        model = models.Genre
        fields = ['genre_title']

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = models.Album
        fields = ['album_title', 'artist', 'genre', 'realeased']

# Testing
class AlbumFormWiki(forms.ModelForm):
    
    class Meta:
        model = models.Album
        fields = ['album_title']
# Testing


class SongForm(forms.ModelForm):
    
    class Meta:
        model = models.Song
        fields = ['song_title', 'position', 'album']

 