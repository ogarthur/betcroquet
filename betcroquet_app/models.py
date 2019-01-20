from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Bet(models.Model):
    pass
    user = models.ManyToManyField(User,related_name='user',on_delete=models.CASCADE)
    #aditional
    name        = models.TextField(max_length=500)
    gameCode    = models.TextField(max_length=500,unique= True)
    state       = models.BooleanField()
    openDate    = models.DateField()
    endDate     = models.DateField()
    max_users   = models.IntegerField()

    def __str__(self):
    return self.name



class Category(models.Model):
    bet = models.ManyToManyField(Bet,related_name='bet',on_delete=models.CASCADE)
    name        = models.TextField(max_length=500)
    description
    winner

    def __str__(self):
    return self.name

    pass

class Option(models.Model):

    category = models.ManyToManyField(Category,related_name='category',on_delete=models.CASCADE)
    name        = models.TextField(max_length=500)
    description
    pass
