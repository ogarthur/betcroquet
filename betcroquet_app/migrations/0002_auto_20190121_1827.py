# Generated by Django 2.1.3 on 2019-01-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betcroquet_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betcollection',
            name='gameCode',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]