# Generated by Django 2.2.7 on 2019-12-04 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdings', '0002_auto_20191202_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_time',
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
