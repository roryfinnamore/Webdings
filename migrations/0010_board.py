# Generated by Django 2.2.7 on 2019-12-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdings', '0009_auto_20191204_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Boards',
            },
        ),
    ]
