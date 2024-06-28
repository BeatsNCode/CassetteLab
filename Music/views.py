from rest_framework import permissions, viewsets
from .models import AppUser, Artist, Track
from .serializers import UserSerializer, ArtistSerializer, TrackSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from dj_rest_auth.views import LoginView as RestAuthLoginView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model

AppUser = get_user_model()

class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    queryset = AppUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserUpdateView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    lookup_field = 'pk'  # Use primary key for lookup

    def get_queryset(self):
        # Ensure the queryset is filtered by the authenticated user
        return AppUser.objects.filter(pk=self.request.user.pk)

    def update(self, request, pk=None):
        # Get the user object using the primary key
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User updated successfully'})
        return JsonResponse(serializer.errors, status=400)
        

class ArtistViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    queryset = Artist.objects.all().order_by('stage_name')
    serializer_class = ArtistSerializer

class ArtistProfileViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ArtistSerializer
    lookup_field = 'user'

    def get_queryset(self):
        user = self.request.user
        return Artist.objects.filter(user=user)
    
class TracksViewset(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Track.objects.all().order_by('title')
    serializer_class = TrackSerializer

    def get_queryset(self):
        user = self.request.user
        return Track.objects.filter(user=user).order_by('title')


class TracksByArtistViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Track.objects.all().order_by('title')
    serializer_class = TrackSerializer

    def get_queryset(self):
        user = self.request.user
        return Track.objects.filter(user=user).order_by('title')
    
class TrackViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = TrackSerializer

    def get_queryset(self):
        user = self.request.user
        return Track.objects.filter(user=user)
    
    def get_object(self):
        queryset = self.get_queryset()
        stage_name = self.kwargs.get("stage_name")  # Assuming you're passing the artist_id in the URL
        track_id = self.kwargs.get("id")  # Assuming you're passing the track_id in the URL
        track = get_object_or_404(queryset, artist_id=stage_name, id=track_id)
        return track
    

class GoogleLoginView(SocialLoginView):

    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000"
    client_class = OAuth2Client
    
class CustomLoginView(RestAuthLoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            # Assuming authentication is successful
            # Set HTTP-only cookie with the authentication token
            response.set_cookie('auth_token', response.data['key'], httponly=False)
        return response


class UserRedirectView(LoginRequiredMixin, RedirectView):
    """
    This view is needed by the dj-rest-auth-library in order to work the google login. It's a bug.
    """
    permanent = False

    def get_redirect_url(self):
        return "redirect-url"
    
