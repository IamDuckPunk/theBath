from django.db import models
import PIL
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='media/profile_images', blank=True)

    def __str__(self):
        return self.user.username







# Create your models here.
