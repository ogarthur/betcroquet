from django.shortcuts import render
from . import forms
from django.utils.translation import gettext as _
#
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user_mgmt_app.forms import UserForm,UserProfileForm
from user_mgmt_app.models import UserProfileInfo
# Create your views here.
##########################################REGISTRO/LOGIN##################################################
#REGISTRO

def register(request):
    registered = False
    if request.method == "POST":
        user_form       = UserForm(data=request.POST)
        profile_form    = UserProfileForm(request.POST,request.FILES)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if(profile.profile_pic=='pic_folder/None/no-img.jpg'):
                profile.profile_pic='profile_pics/avatar.png'
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'user_mgmt_app/registration.html',
    {'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered})

#LOGIN
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                user_info=UserProfileInfo.objects.filter(user=user).values_list('profile_pic',flat=True)
                request.session['profile_pic']=user_info[0]
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Cuenta no activa")
        else:
            print("Someone tried to login and failed")
            print("Username: {}  with password :{}".format(username,password))
            return render(request,'user_mgmt_app/login.html',{'login_error':'Credeenciales no válidos'})
    else:
        return render(request,'user_mgmt_app/login.html',{})


#LOGOUT
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
