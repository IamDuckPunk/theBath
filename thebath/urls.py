from django.conf.urls import url, include
from django.contrib import admin
import django.views.defaults
from django.conf import settings
from django.conf.urls.static import static
from Music.views import search_albums
from Account import views as account_views


urlpatterns = [

    #thebath/admin/
    url(r'^admin/', admin.site.urls),

    url(r'register/$', account_views.register, name='register'),

    url(r'login/$', account_views.user_login, name='login'),
    url(r'logout/$', account_views.user_logout, name='logout'),

    # thebath/search/?q=since
    url(r'^search/$', search_albums, name='search_albums'),

    #thebath/albums/
    url(r'^', include('Music.urls')),

    #thebath/profiles/
    url(r'^profiles/', include('Account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
