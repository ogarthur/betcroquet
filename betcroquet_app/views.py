from django.shortcuts import render
from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
#
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from user_mgmt_app.models import  UserProfileInfo,FriendRelationship
from betcroquet_app.models import BetCollection,Bet,BetTemplate
from user_mgmt_app.forms import  FriendForm
from betcroquet_app import forms as betForms
from betcroquet_app.forms import AddBetForm
# Create your views here.
def index(request):
    if  request.user.is_authenticated:
        addBetForm = betForms.AddBetForm()
        if request.method == 'POST':
            addBet = betForms.AddBetForm(data=request.POST)
            if addBet.is_valid():
                post_gameCode = request.POST.get('gameCode')
                print('==================================================',post_gameCode)
                if ( BetCollection.objects.filter(gameCode=post_gameCode ).count()>0):
                    if  Bet.objects.filter(user =request.user).count()>0:
                        print("YA AÑADIDA")
                    else:
                        bet_collection = BetCollection.objects.get(gameCode=post_gameCode)
                        new_bet = Bet(betCollection=bet_collection,user=request.user)
                        new_bet.save()
                        print("Bet added to user")
                return redirect('index')
        else:
            return render(request,'betcroquet_app/index.html',{'addBetForm':addBetForm})
    else:
        return render(request,'betcroquet_app/index.html')
