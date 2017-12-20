from django.conf.urls import url
from Music import views as mus_views

urlpatterns = [
    # thebath/index/
    url(r'^$', mus_views.index),

    # thebath/albums/
    url(r'albums/$', mus_views.albums, name='albums'),

    # thebath/albums/12/
    url(r'^albums/(?P<album_id>[0-9]+)/$',
        mus_views.details_album, name='details_album'),

    # thebath/albums/12/favourite/
    url(r'^albums/(?P<album_id>[0-9]+)/favourite/$',
        mus_views.favourite_album, name='favourite_album'),

    # thebath/albums/12/delete/
    url(r'^albums/(?P<album_id>[0-9]+)/delete/$',
        mus_views.delete_album, name='delete_album'),

    # thebath/albums/create_album/
    url(r'^albums/create_album/$', mus_views.create_album_wiki, name='create_album'),

    # thebath/artists/
    url(r'^artists/$', mus_views.artists, name='artists'),

    # thebath/artists/12/
    url(r'^artists/(?P<artist_id>[0-9]+)/$',
        mus_views.details_artist, name='details_artist'),

    # thebath/artists/12/delete/
    url(r'^artists/(?P<artist_id>[0-9]+)/delete/$',
        mus_views.delete_artist, name='delete_artist'),

    # Testing
    # thebath/artists/12/create_album/
    #url(r'^artists/(?P<artist_id>[0-9]+)/create_album/$', mus_views.create_album, name='artist_create_album'),
    # Testing

    # thebath/create_artist/
    url(r'^artists/create_artist/$', mus_views.create_artist, name='create_artist'),

    # thebath/genres/
    url(r'^genres/$', mus_views.genres, name='genres'),

    # thebath/genres/21/
    url(r'^genres/(?P<genre_id>[0-9]+)/$',
        mus_views.details_genre, name='details_genre'),

    # thebath/genres/21/
    url(r'^genres/(?P<genre_id>[0-9]+)/delete/$',
        mus_views.delete_genre, name='delete_genre'),

    # thebath/create_genre/
    url(r'^genres/create_genre/$', mus_views.create_genre, name='create_genre'),

    # thebath/about/
    url(r'about/$', mus_views.about, name='about'),

]
