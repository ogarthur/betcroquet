from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class BetCollection(models.Model):
    gameCode    = models.TextField(max_length=500,unique= True)
    state       = models.BooleanField(default = False)
    openDate    = models.DateField()
    endDate     = models.DateField()
    max_users   = models.IntegerField(null=True)
    name        = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Bet(models.Model):
    betCollection   = models.ForeignKey(BetCollection,related_name='betCollBet',on_delete=models.CASCADE)
    user            = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    hits            = models.IntegerField(default=0)

class Category(models.Model):
    bet             = models.ForeignKey(Bet,related_name='bet',on_delete=models.CASCADE)
    betCollection   = models.ForeignKey(BetCollection,related_name='betCollCategory',on_delete=models.CASCADE)
    name            = models.TextField(max_length=300)
    description     = models.TextField(max_length=900,null=True)
    #winner      = models.ForeignKey(Option,related_name='option',null=True)
    image           = models.ImageField(upload_to = 'category_pics/', default = 'category_pics/None/no-img.jpg')
    def __str__(self):
        return self.name

class Option(models.Model):

    category    = models.ManyToManyField(Category,related_name='optionCategory')
    name        = models.TextField(max_length=500)
    description = models.TextField(max_length=900,null=True)
    image       = models.ImageField(upload_to = 'option_pics/', default = 'option_pics/None/no-img.jpg')
    video       = models.TextField(max_length=900,null=True)

class CategoryWinner(models.Model):
    category    = models.ForeignKey(Category,on_delete = models.CASCADE)
    option      = models.ForeignKey(Option,on_delete = models.CASCADE)
