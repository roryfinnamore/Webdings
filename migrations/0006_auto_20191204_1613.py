# Generated by Django 2.2.7 on 2019-12-04 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webdings', '0005_auto_20191204_1612'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Guests',
            new_name='Guest',
        ),
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]
