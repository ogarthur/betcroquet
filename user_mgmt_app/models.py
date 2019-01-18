from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #aditional
    user_info = models.TextField(max_length=500,blank=True)

    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
    def __str__(self):
        return self.user.username
