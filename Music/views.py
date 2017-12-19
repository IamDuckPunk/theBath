from django.shortcuts import render, get_object_or_404
from . import models as music_models
from . import forms as music_forms


def albums(request):
    # Pass list of albums into template
    albums_list = music_models.Album.objects.order_by('album_title')[:30]
    args = {'Albums': albums_list}
    return render(request, 'music/albums.html', args)


def artists(request):
    # Pass list of artists into template
    artists_list = music_models.Artist.objects.order_by('artist')[:30]
    args = {'Artists': artists_list}
    return render(request, 'music/artists.html', args)


def genres(request):
    # Pass list of genres into template
    genres_list = music_models.Genre.objects.order_by('genre_title')[:30]
    args = {'Genres': genres_list}
    return render(request, 'music/genres.html', args)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def details_album(request, album_id):

    album = get_object_or_404(music_models.Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def details_artist(request, artist_id):

    artist = get_object_or_404(music_models.Artist, pk=artist_id)
    return render(request, 'music/detail_artist.html', {'artist': artist})


def details_genre(request, genre_id):

    genre = get_object_or_404(music_models.Genre, pk=genre_id)
    return render(request, 'music/detail_genre.html', {'genre': genre})


def favourite_album(request, album_id):

    album = get_object_or_404(music_models.Album, pk=album_id)
    if album.is_favourite == True:
        album.is_favourite = False
    elif album.is_favourite == False:
        album.is_favourite = True
    album.save()
    return render(request, 'music/albums.html', {'album': album})


def favourite_artist(request, artist_id):
    pass


def favourite_genre(request, genre_id):
    pass


def create_artist(request):

    form = music_forms.ArtistForm(request.POST or None)
    if form.is_valid():
        artist = form.save(commit=False)
        artist.save()
        return render(request, 'music/detail_artist.html', {'artist': artist})
    else:
        context = {
            "form": form,
        }
        return render(request, 'music/create_artist.html', context)


def create_genre(request):

    form = music_forms.GenreForm(request.POST or None)
    if form.is_valid():
        genre = form.save(commit=False)
        genre.save()
        return render(request, 'music/detail_genre.html', {'genre': genre})
    else:
        context = {
            "form": form,
        }
        return render(request, 'music/create_genre.html', context)


def create_album(request):

    form = music_forms.AlbumForm(request.POST or None) # bunch of html code
    if form.is_valid():
        album = form.save(commit=False)
        print(album)
        album.save()
        return render(request, 'music/detail.html', {'album': album})
    else:
        context = {
            "form": form,
        }
        return render(request, 'music/create_album.html', context)

def delete_genre(request, genre_id):
    genre = music_models.Genre.objects.get(pk=genre_id)
    genre.delete()
    return render(request, 'music/genres.html', {'genre': genre})


def delete_album(request, album_id):
    album = music_models.Album.objects.get(pk=album_id)
    album.delete()
    return render(request, 'music/albums.html', {'album': album})


def delete_artist(request, artist_id):
    artist = music_models.Artist.objects.get(pk=artist_id)
    artist.delete()
    return render(request, 'music/artists.html', {'artist': artist})
