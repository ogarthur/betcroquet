from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class BetTemplate(models.Model):

    name        = models.CharField(max_length = 100)
    description = models.TextField(max_length=500,null=True)
    state       = models.BooleanField(default = False)
    openDate    = models.DateField(null=True)
    endDate     = models.DateField(null=False)


    def __str__(self):
        return self.name

class BetCollection(models.Model):

    """Collection of the bets of users"""
    gameCode    = models.CharField(max_length=100,unique= True)
    name        = models.CharField(max_length=100)
    closeDate   = models.DateField(null=True)
    max_users   = models.IntegerField(null=True)
    description = models.TextField(max_length=500,null=True)

    template    = models.ForeignKey(BetTemplate,related_name="betCollTemplate",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{}:{}'.format(self.gameCode,self.name)



class Bet(models.Model):

    """user personal bet"""
    betCollection   = models.ForeignKey(BetCollection,related_name='betCollBet',on_delete=models.CASCADE)
    user            = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    hits            = models.IntegerField(default=0)
    def __str__(self):
        return 'User:{}, Game:{}'.format(self.user.username,self.betCollection.gameCode)



class Category(models.Model):

    BetTemplate     = models.ForeignKey(BetTemplate,related_name='BetTemplateCategory',on_delete=models.CASCADE,null=True)
    name            = models.TextField(max_length=300)
    description     = models.TextField(max_length=900,null=True,blank=True)
    #winner      = models.ForeignKey(Option,related_name='option',null=True)
    image           = models.ImageField(upload_to = 'category_pics/', default = 'category_pics/None/no-img.jpg')
    def __str__(self):
        return self.name

class Option(models.Model):

    category    = models.ManyToManyField(Category,related_name='optionCategory')
    name        = models.TextField(max_length=500)
    description = models.TextField(max_length=900,null=True,blank=True)
    image       = models.ImageField(upload_to = 'option_pics/', default = 'option_pics/None/no-img.jpg')
    video       = models.TextField(max_length=900,null=True,blank=True)
    def __str__(self):
        return self.name

class BetSelection(models.Model):
    """actual user selection"""
    bet         = models.OneToOneField(Bet,related_name = 'betSelection',on_delete = models.CASCADE)
    category    = models.OneToOneField(Category,related_name = 'categoryBet',on_delete = models.CASCADE)
    option      = models.OneToOneField(Option,related_name = 'optionBet',on_delete = models.CASCADE)
    def __str__(self):
        return 'user:{},c:{},o:{}'.format(self.bet.user.username,self.category.name,self.option.name) 

class CategoryWinner(models.Model):
    category    = models.ForeignKey(Category,on_delete = models.CASCADE)
    option      = models.ForeignKey(Option,on_delete = models.CASCADE)
