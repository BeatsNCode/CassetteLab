from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .managers import UserManager


# Create your models here.
class AppUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
   
class Genre(models.Model):
    genre = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.genre

class Artist(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, default=list)
    
    def __str__(self):
        return self.stage_name

class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='tracks/')
    duration = models.DurationField()
    plays = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_art = models.ImageField(upload_to='album_covers/', blank=True)
    tracks = models.ManyToManyField(Track, blank=True)
    genres = models.ManyToManyField(Genre, default=list)
    
    def __str__(self):
        return self.title

class AlbumTrack(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()

    def __str__(self):
        return self.track
    
class ExtendedPlaylist(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_art = models.ImageField(upload_to='playlist_covers/', blank=True)
    tracks = models.ManyToManyField(Track, blank=True)
    genres = models.ManyToManyField(Genre, default=list)

    def __str__(self):
        return self.title

class PlaylistTrack(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    playlist = models.ForeignKey(ExtendedPlaylist, on_delete=models.CASCADE)
    track_order = models.PositiveIntegerField()

    def __str__(self):
        return self.track
