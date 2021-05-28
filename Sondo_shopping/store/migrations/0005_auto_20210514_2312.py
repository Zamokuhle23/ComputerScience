# Generated by Django 3.2.2 on 2021-05-14 20:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210514_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_connected',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 14, 23, 12, 18, 260613)),
        ),
    ]
