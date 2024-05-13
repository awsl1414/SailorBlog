from django.urls import path

from .views import UserRegistrationView, AvatarUploadView, CustomObtainAuthToken

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("avatar/", AvatarUploadView.as_view(), name="avatar"),
    path("login/", CustomObtainAuthToken.as_view(), name="login"),
]
