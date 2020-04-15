import datetime
from django.db import models
from django.utils import timezone

class Album(models.Model): #can add more fields later
    album_title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date of release')
    def __str__(self):
        return self.album_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Song(models.Model):
    song_title = models.CharField(max_length=75)
    album = models.ForeignKey(Album, on_delete = models.CASCADE) #many songs to one album
    def __str__(self):
        return self.song_title  