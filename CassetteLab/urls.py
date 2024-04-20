from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Music import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'Artists', views.ArtistViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('music/', include("Music.urls")),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
