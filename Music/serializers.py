from django.conf import settings
from .models import Artist, Track
from rest_framework import serializers

AppUser = settings.AUTH_USER_MODEL

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'email', 'password', 'visits']
    
    def to_representation(self, instance):
        if instance.is_superuser:
        # If the user is a superuser, return an empty representation
            return {}
        return super().to_representation(instance)

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer

    class Meta:
        model= Artist
        fields = ['id', 'user', 'stage_name', 'location', 'genres',]

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    user = ArtistSerializer

    class Meta:
        model=Track
        fields = ['title', 'artist', 'audio_file', 'duration', 'plays', ]
