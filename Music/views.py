from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .models import Artist, Track
from .serializers import UserSerializer, ArtistSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('stage_name')
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]