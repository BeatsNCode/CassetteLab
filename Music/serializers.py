from django.conf import settings
from .models import Artist, Track
from rest_framework import serializers

AppUser = settings.AUTH_USER_MODEL

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        user_id = serializers.IntegerField(source='id', read_only=True)


        fields = ['user_id', 'email']
    
    def to_representation(self, instance):
        if instance.is_superuser:
        # If the user is a superuser, return an empty representation
            return {}
        return super().to_representation(instance)

class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer
    user_id = serializers.IntegerField(source='id', read_only=True)


    class Meta:
        model= Artist
        fields = ['user_id', 'stage_name', 'location', 'genres',]

class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(source='artist.stage_name')
    user_id = serializers.IntegerField(source='id', read_only=True)
    track_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model=Track
        fields = ['track_id', 'user_id','title', 'artist', 'audio_file', 'duration', 'plays', ]

