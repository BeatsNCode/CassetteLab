from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Music import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from dj_rest_auth.views import PasswordResetView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'artist', views.ArtistProfileViewSet, basename='artists')
router.register(r'tracks', views.TracksViewset, basename='tracks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('tracks/<int:track_id>/', views.TrackViewSet.as_view({'get': 'retrieve'}), name='track-detail'),
    path('artist/<int:user>/', views.ArtistProfileViewSet.as_view({'get': 'retrieve'}), name='artist-detail'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view({'put': 'update'}), name='user-update'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),  
    path('auth/', include('django.contrib.auth.urls')),  
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
