from django.db import models
import PIL
from django.contrib.auth.models import User
from django.urls import reverse
from Music.models import Album

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, default='')
    last_name = models.CharField(max_length=30, default='')
    user_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
    birth_date = models.DateField(null=True)

    favourite_albums = models.ManyToManyField(Album, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user': self.user.username})




