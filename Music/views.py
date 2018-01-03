from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from . import models as music_models
from . import forms as music_forms
from .parsers import parse, create_wiki_songs
from Account.models import UserProfile
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from Account.models import UserProfile

@login_required
def albums(request):
    # Pass list of albums into template
    albums_list = music_models.Album.objects.annotate(fav=Count('userprofile')).order_by('-fav')[:30]
    userprofile = UserProfile.objects.get(pk=request.user.id)
    args = {
        'Albums': albums_list,
        'userprofile': userprofile
    }
    return render(request, 'music/albums.html', args)

@login_required
def artists(request):
    # Pass list of artists into template
    artists_list = music_models.Artist.objects.order_by('artist')[:30]
    args = {'Artists': artists_list}
    return render(request, 'music/artists.html', args)

@login_required
def genres(request):
    # Pass list of genres into template
    genres_list = music_models.Genre.objects.order_by('genre_title')[:30]
    args = {'Genres': genres_list}
    return render(request, 'music/genres.html', args)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

@login_required
def details_album(request, pk):

    album = get_object_or_404(music_models.Album, pk=pk)
    create_wiki_songs(album)
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

@login_required
def details_artist(request, pk):

    artist = get_object_or_404(music_models.Artist, pk=pk)
    return render(request, 'music/detail_artist.html', {'artist': artist})

@login_required
def details_genre(request, pk):

    genre = get_object_or_404(music_models.Genre, pk=pk)
    return render(request, 'music/detail_genre.html', {'genre': genre})

@login_required
def favourite_album(request, album_id):
    try:
        album = get_object_or_404(music_models.Album, pk=album_id)
        current_user = request.user
        userprofile = get_object_or_404(UserProfile, pk=current_user.id)
        if album in userprofile.favourite_albums.all():
            userprofile.favourite_albums.remove(album)
            print('Album %s removed' % str(album))
            userprofile.save()
        else:
            userprofile.favourite_albums.add(album)
            print('Album %s added' % str(album))
            userprofile.save()
        return redirect('/albums/')

    except Exception:
        return redirect('/albums/')

    
@login_required
def favourite_artist(request, artist_id):
    artist = get_object_or_404(music_models.Artist, pk=artist_id)
    if artist.is_favourite == True:
        artist.is_favourite = False
    elif artist.is_favourite == False:
        artist.is_favourite = True
    artist.save()
    return redirect('/artists/')

@login_required
def favourite_genre(request, genre_id):

    genre = get_object_or_404(music_models.Genre, pk=genre_id)
    if genre.is_favourite == True:
        genre.is_favourite = False
    elif genre.is_favourite == False:
        genre.is_favourite = True
    genre.save()
    return redirect('/genres/')

@login_required
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

@login_required
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

@login_required
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

@login_required
def delete_genre(request, genre_id):
    genre = music_models.Genre.objects.get(pk=genre_id)
    genre.delete()
    return render(request, 'music/genres.html', {'genre': genre})

@login_required
def delete_album(request, album_id):
    album = music_models.Album.objects.get(pk=album_id)
    album.delete()
    return render(request, 'music/albums.html', {'album': album})

@login_required
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


@login_required
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


