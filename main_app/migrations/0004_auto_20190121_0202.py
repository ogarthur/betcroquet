# Generated by Django 2.1.3 on 2019-01-21 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20181122_0157'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='GameTemplate',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]