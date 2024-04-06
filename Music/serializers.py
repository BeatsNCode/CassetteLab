from django.contrib.auth.models import User
from .models import Artist
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model= Artist
        fields = ['id', 'user', 'stage_name', 'biography', 'location']