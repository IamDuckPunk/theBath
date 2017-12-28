from django.conf.urls import url, include
from Music import views as mus_views
from . import forms as music_forms

urlpatterns = [
    # thebath/index/
    url(r'^$', mus_views.index),

    # thebath/albums/
    url(r'albums/$', mus_views.albums, name='albums'),

    # thebath/albums/12/
    url(r'^albums/(?P<pk>\d+)/$',
        mus_views.details_album, name='details_album'),

    # thebath/albums/12/favourite/
    url(r'^albums/(?P<album_id>[0-9]+)/favourite/$',
        mus_views.favourite_album, name='favourite_album'),

    # thebath/albums/12/delete/
    url(r'^albums/(?P<album_id>[0-9]+)/delete/$',
        mus_views.delete_album, name='delete_album'),

    # thebath/albums/create_album/
    url(r'^albums/create_album/$', mus_views.create_album, name='create_album'),

     # thebath/albums/12/edit/
    url(r'^albums/(?P<pk>\d+)/edit/$',
        music_forms.AlbumFormUpdate.as_view(), name='edit_album'),

    # thebath/artists/
    url(r'^artists/$', mus_views.artists, name='artists'),

    # thebath/artists/12/
    url(r'^artists/(?P<pk>\d+)/$',
        mus_views.details_artist, name='details_artist'),
    
    # thebath/artists/12/favourite/
    url(r'^artists/(?P<artist_id>[0-9]+)/favourite/$',
        mus_views.favourite_artist, name='favourite_artist'),

    # thebath/artists/12/delete/
    url(r'^artists/(?P<artist_id>[0-9]+)/delete/$',
        mus_views.delete_artist, name='delete_artist'),

    # thebath/create_artist/
    url(r'^artists/create_artist/$', mus_views.create_artist, name='create_artist'),

    # thebath/artists/12/edit/
    url(r'^artists/(?P<pk>\d+)/edit/$',
       music_forms.ArtistFormUpdate.as_view(), name='edit_artist'),

    # thebath/genres/
    url(r'^genres/$', mus_views.genres, name='genres'),

    # thebath/genres/21/
    url(r'^genres/(?P<pk>\d+)/$',
        mus_views.details_genre, name='details_genre'),

     # thebath/genres/12/favourite/
    url(r'^genres/(?P<genre_id>[0-9]+)/favourite/$',
        mus_views.favourite_genre, name='favourite_genre'),

    # thebath/genres/21/delete/
    url(r'^genres/(?P<genre_id>[0-9]+)/delete/$',
        mus_views.delete_genre, name='delete_genre'),

    # thebath/create_genre/
    url(r'^genres/create_genre/$', mus_views.create_genre, name='create_genre'),

    # thebath/about/
    url(r'about/$', mus_views.about, name='about'),

   
    
   
]
