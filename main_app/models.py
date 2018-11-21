from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete="cascade")
    #aditional
    nick            = models.CharField(max_length=200,blank=True)
    profile_pic     = models.ImageField(upload_to='profile_pics',blank=True)
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
    def __str__(self):
        return self.user.username

class Game(models.Model):
    pass

class GameTemplate(models.Model):
    pass

class Section(models.Model):
    pass

class Option(models.Model):

    pass
 
