# Generated by Django 2.1.1 on 2018-11-28 16:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_mgmt_app', '0002_friendrelatioship'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendRelatioship',
            new_name='FriendRelationship',
        ),
    ]
