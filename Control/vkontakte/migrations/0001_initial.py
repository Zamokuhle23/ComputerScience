# Generated by Django 3.2 on 2021-04-19 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(verbose_name='date_of_birth')),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(verbose_name='date published')),
                ('title', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=9000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vkontakte.user')),
                ('likes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vkontakte.likes')),
            ],
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vkontakte.user'),
        ),
    ]
