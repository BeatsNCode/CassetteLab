from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    pass

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.stage_name

class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='tracks/')
    duration = models.DurationField()
    plays = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_art = models.ImageField(upload_to='album_covers/')
    tracks = models.ManyToManyField(Track, blank=True)

class AlbumTrack(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()

class ExtendedPlaylist(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_art = models.ImageField(upload_to='playlist_covers/', blank=True)
    tracks = models.ManyToManyField(Track, blank=True)

class PlaylistTrack(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    playlist = models.ForeignKey(ExtendedPlaylist, on_delete=models.CASCADE)
    track_order = models.PositiveIntegerField()
