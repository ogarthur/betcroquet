# Generated by Django 2.1.3 on 2018-11-22 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20181121_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
