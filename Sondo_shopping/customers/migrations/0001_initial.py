# Generated by Django 3.2.2 on 2021-06-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', upload_to='profile_pics')),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(default='shopping12345', max_length=30)),
            ],
        ),
    ]