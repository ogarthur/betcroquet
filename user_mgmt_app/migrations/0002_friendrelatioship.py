# Generated by Django 2.1.1 on 2018-11-28 12:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_mgmt_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRelatioship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete='null', related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete='null', related_name='userCreator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
