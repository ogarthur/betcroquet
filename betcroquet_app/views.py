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
        #FIRST CHECK ALL BETS FROM USER
        #SECOND ADD FORM TO ADD Bet
        #THIRD ADD FORM TO CREATE BET
        user_bets           = Bet.objects.filter(user=request.user).values()
        bet_cards           = []
        bet_cards_completed = []
        addBetForm  = betForms.AddBetForm()
        data = {}
        data['addBetForm'] = addBetForm
        for bet in user_bets:

            bet_collection = BetCollection.objects.get(pk= bet['betCollection_id'])
            bet_template    = BetTemplate.objects.get(  pk = bet_collection.template.id)
            card ={'template':bet_template.name,
                   'templateDes':bet_template.description,
                   'name':bet_collection.name,
                   'gameCode':bet_collection.gameCode,
                   'collectionDes':bet_collection.description,
                   'closeDate':bet_collection.closeDate,
                   'state':bet_template.state,
                   'image':('/media/{}').format(bet_template.image),}
            if card['state']:
                bet_cards_completed.append(card)
            else:
                bet_cards.append(card)



        data['bet_cards'] = bet_cards
        data['bet_cards_completed'] = bet_cards_completed
        if request.method == 'POST':
            addBet = betForms.AddBetForm(data=request.POST)

            if addBet.is_valid():
                post_gameCode = request.POST.get('gameCode')
                print('==================================================',post_gameCode)
                if ( BetCollection.objects.filter(gameCode=post_gameCode ).count()>0):
                    bet_collection = BetCollection.objects.get(gameCode=post_gameCode)
                    if  Bet.objects.filter(user =request.user,betCollection= bet_collection).count()>0:
                        print("YA AÑADIDA")
                    else:
                        new_bet = Bet(betCollection=bet_collection,user=request.user)
                        new_bet.save()
                        print("Bet added to user")


        return render(request,'betcroquet_app/index.html',data)
    else:
        return render(request,'betcroquet_app/index.html')

def betview(request,gameCode):
    return render(request,'betcroquet_app/betform.html')

def addBetview(request):
    return render(request,'betcroquet_app/addbet.html')
