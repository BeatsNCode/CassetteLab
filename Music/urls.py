from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView
from Music.views import GoogleLoginView, UserRedirectView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
        path("dj-rest-auth/google/login/", GoogleLoginView.as_view(), name="google_login"),
        path("~redirect/", view=UserRedirectView.as_view(), name="redirect")
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('logout/', LogoutView.as_view()),
    # path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    # path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
]