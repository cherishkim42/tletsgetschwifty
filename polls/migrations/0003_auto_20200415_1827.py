# Generated by Django 3.0.5 on 2020-04-15 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_album_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
