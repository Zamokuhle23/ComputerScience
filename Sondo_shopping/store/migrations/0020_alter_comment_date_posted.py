# Generated by Django 3.2.2 on 2021-05-26 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_comment_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 26, 16, 23, 36, 452695)),
        ),
    ]