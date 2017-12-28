from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models


class ArtistForm(forms.ModelForm):

    class Meta:
        model = models.Artist
        fields = ['artist']


class ArtistFormUpdate(UpdateView):
    
    model = models.Artist
    fields = ['artist']
    template_name = 'music/create_artist.html'
    def get_success_url(self):
        return reverse_lazy('details_artist', kwargs={'pk': self.get_object().id})
    
        

class GenreForm(forms.ModelForm):

    class Meta:
        model = models.Genre
        fields = ['genre_title']


class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = models.Album
        fields = ['album_title', 'artist', 'genre', 'realeased']
    

class AlbumFormUpdate(UpdateView):
    
    model = models.Album
    fields = ['album_title', 'artist', 'genre', 'realeased']
    template_name = 'music/album_form.html'

    def get_success_url(self):
        return reverse_lazy('details_album', kwargs={'pk': self.get_object().id})

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

 