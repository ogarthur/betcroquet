from django.shortcuts import render
from django.utils.translation import gettext as _
#
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from user_mgmt_app.models import  UserProfileInfo,FriendRelationship
from user_mgmt_app.forms import  FriendForm
# Create your views here.
def index(request):
    return render(request,'betcroquet_app/index.html')
