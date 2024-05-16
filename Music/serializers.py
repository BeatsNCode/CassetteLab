from django.conf import settings
from .models import Artist, Track
from rest_framework import serializers

AppUser = settings.AUTH_USER_MODEL

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'email']
    
    def to_representation(self, instance):
        if instance.is_superuser:
        # If the user is a superuser, return an empty representation
            return {}
        return super().to_representation(instance)

class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model= Artist
        fields = ['user', 'stage_name', 'location', 'genres',]

class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(source='artist.stage_name')
    

    class Meta:
        model=Track
        fields = ['id', 'user','title', 'artist', 'audio_file', 'duration', 'plays', ]

