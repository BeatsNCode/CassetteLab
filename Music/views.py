from django.conf import settings
from rest_framework import permissions, viewsets
from .models import AppUser, Artist, Track
from .serializers import UserSerializer, ArtistSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# User = settings.AUTH_USER_MODEL

class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('stage_name')
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
