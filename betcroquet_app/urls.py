from django.contrib import admin
from django.urls import path,include
from betcroquet_app import views
#template tag
app_name = 'betcroquet_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('bet/<int:gameCode>',views.betview,name='betView'),
    path('addBet',views.addBetview,name='addBetview'),
    #path('register/',views.register,name='register'),
    #path('user_login/',views.user_login,name='user_login'),

]
