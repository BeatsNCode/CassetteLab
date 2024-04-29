from django.conf import settings
from .models import Artist
from rest_framework import serializers

User = settings.AUTH_USER_MODEL

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
    
    def to_representation(self, instance):
        if instance.is_superuser:
        # If the user is a superuser, return an empty representation
            return {}
        return super().to_representation(instance)

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model= Artist
        fields = ['id', 'user', 'stage_name', 'biography', 'location', 'genres']