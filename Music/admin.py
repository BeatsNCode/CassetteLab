from django.contrib import admin 
from Music.models import Artist, Track
from django.contrib.auth.models import Group

# Register your models here.
class TrackInline(admin.TabularInline):
    model = Track
    extra = 0

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [TrackInline]

class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'duration']

admin.site.unregister(Group)