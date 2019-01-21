from django.contrib import admin

# Register your models here.
from user_mgmt_app.models import UserProfileInfo,FriendRelationship
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(FriendRelationship)
