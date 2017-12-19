from django.contrib import admin
from Music.models import *

admin.site.register((Artist, Album, Song, Genre))
# Register your models here.
