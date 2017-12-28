from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from . import models as music_models
from . import forms as music_forms
from .parsers import parse
from Account.models import UserProfile
from django.db.models import Q


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


def details_album(request, pk):

    album = get_object_or_404(music_models.Album, pk=pk)
    try:
        info, headers, songs = parse(str(album))

    except Exception as err:
        print(err)
        args = {
            'album': album,
            'info': None,
            'headers': None,
            'songs': None,
        }
    else:
        args = {
            'album': album,
            'info': info,
            'headers': headers,
            'songs': songs,
        }
    return render(request, 'music/detail.html', args)


def details_artist(request, pk):

    artist = get_object_or_404(music_models.Artist, pk=pk)
    return render(request, 'music/detail_artist.html', {'artist': artist})


def details_genre(request, pk):

    genre = get_object_or_404(music_models.Genre, pk=pk)
    return render(request, 'music/detail_genre.html', {'genre': genre})


def favourite_album(request, album_id):

    album = get_object_or_404(music_models.Album, pk=album_id)
    if album.is_favourite == True:
        album.is_favourite = False
    elif album.is_favourite == False:
        album.is_favourite = True
    album.save()
    return redirect('/albums/')


def favourite_artist(request, artist_id):
    artist = get_object_or_404(music_models.Artist, pk=artist_id)
    if artist.is_favourite == True:
        artist.is_favourite = False
    elif artist.is_favourite == False:
        artist.is_favourite = True
    artist.save()
    return redirect('/artists/')


def favourite_genre(request, genre_id):

    genre = get_object_or_404(music_models.Genre, pk=genre_id)
    if genre.is_favourite == True:
        genre.is_favourite = False
    elif genre.is_favourite == False:
        genre.is_favourite = True
    genre.save()
    return redirect('/genres/')


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

    form = music_forms.AlbumForm(request.POST or None)  # bunch of html code
    if form.is_valid():
        album = form.save(commit=False)
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

# TESTING
def create_album_wiki(request):

    form = music_forms.AlbumFormWiki(
        request.POST or None)  # bunch of html code
    if form.is_valid():
        album = form.save(commit=False)
        album.save()
        return render(request, 'music/detail.html', {'album': album})
    else:
        context = {
            "form": form,
        }
        return render(request, 'music/create_album.html', context)



def search_albums(request):
    query = request.GET.get("q")
    print(query)
    if query:
        albums = music_models.Album.objects.filter(
            Q(album_title__icontains=query)
        ).distinct()
        artists = music_models.Artist.objects.filter(
            Q(artist__icontains=query)
        ).distinct()
        genres = music_models.Genre.objects.filter(
            Q(genre_title__icontains=query)
        ).distinct()
        args = {
            'albums': albums,
            'artists': artists,
            'genres': genres,
        }
        return render(request, 'search.html', args)
    else:
        err = "Nothing was typed"
        return render(request, 'search.html', {'err':err})



