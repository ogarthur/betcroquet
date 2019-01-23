# Generated by Django 2.1.3 on 2019-01-21 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betcroquet_app', '0003_auto_20190121_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='betSelection', to='betcroquet_app.Bet')),
            ],
        ),
        migrations.CreateModel(
            name='BetTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True)),
                ('state', models.BooleanField(default=False)),
                ('openDate', models.DateField(null=True)),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='betcollection',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='betcollection',
            name='openDate',
        ),
        migrations.RemoveField(
            model_name='betcollection',
            name='state',
        ),
        migrations.AddField(
            model_name='betcollection',
            name='closeDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='description',
            field=models.TextField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='video',
            field=models.TextField(blank=True, max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='betselect',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='categoryBet', to='betcroquet_app.Category'),
        ),
        migrations.AddField(
            model_name='betselect',
            name='option',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='optionBet', to='betcroquet_app.Option'),
        ),
        migrations.AddField(
            model_name='betcollection',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='betCollTemplate', to='betcroquet_app.BetTemplate'),
        ),
    ]