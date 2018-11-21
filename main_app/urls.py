from django.contrib import admin
from django.urls import path,include
from main_app import views
#template tag
app_name = 'main_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

]
