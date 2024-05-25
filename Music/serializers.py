from django.conf import settings
from .models import Artist, Track
from rest_framework import serializers

AppUser = settings.AUTH_USER_MODEL

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser

        fields = ['email']
    
    def to_representation(self, instance):
        if instance.is_superuser:
        # If the user is a superuser, return an empty representation
            return {}
        return super().to_representation(instance)

class ArtistSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(source='user', read_only=True)
    user = UserSerializer

    class Meta:
        model= Artist

        fields = ['user', 'stage_name', 'location', 'genres',]

class TrackSerializer(serializers.ModelSerializer):
    user = ArtistSerializer
    stage_name = serializers.CharField(source='artist.stage_name')
    track_id = serializers.IntegerField(source='id', read_only=True)


    class Meta:
        model=Track
        fields = ['track_id', 'title', 'stage_name', 'audio_file', 'duration', 'plays',]

