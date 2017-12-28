from django.conf.urls import url, include
from django.contrib import admin
import django.views.defaults
from django.conf import settings
from django.conf.urls.static import static
from Music.views import search_albums


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # thebath/search/?q=since
    url(r'^search/$', search_albums, name='search_albums'),
    url(r'^', include('Music.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
