from django.urls import path

from .views import UserRegistrationView, AvatarUploadView, CustomObtainAuthToken

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("avatar/", AvatarUploadView.as_view(), name="avatar-upload"),
    path("login/", CustomObtainAuthToken.as_view(), name="user-login"),
]
