# Generated by Django 2.1.3 on 2019-01-21 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betcroquet_app', '0005_auto_20190121_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='bet',
        ),
        migrations.RemoveField(
            model_name='category',
            name='betCollection',
        ),
        migrations.AddField(
            model_name='category',
            name='BetTemplate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BetTemplateCategory', to='betcroquet_app.BetTemplate'),
        ),
    ]
