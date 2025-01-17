from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="userInfo")

    #aditional
    user_info    = models.TextField(max_length=500,blank=True)
    profile_pic   = models.ImageField(upload_to = 'profile_pics/', default = 'pic_folder/None/no-img.jpg')
    language     = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
    def __str__(self):
        return self.user.username

class FriendRelationship(models.Model):
    user   = models.ForeignKey(User,related_name="userCreator",on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friends",on_delete=models.CASCADE)
