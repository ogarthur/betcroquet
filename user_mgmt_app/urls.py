from django.contrib import admin
from django.urls import path,include
from user_mgmt_app import views
#template tag
app_name = 'user_mgmt_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
]
