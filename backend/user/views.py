from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model


from .serializers import UserRegistrationSerializer, AvatarSerializer

User = get_user_model()


@extend_schema(
    summary="用户注册",
    request=UserRegistrationSerializer,
    responses={201: UserRegistrationSerializer},
)
class UserRegistrationView(APIView):
    def post(self, requset, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=requset.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user).key
            data = {
                "message": "用户注册成功。",
                "user": user.username,
                "token": token,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvatarUploadView(generics.UpdateAPIView):
    serializer_class = AvatarSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]  # 有坑，django官方把 bearer 替换成了 token
    parser_classes = [MultiPartParser]

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "头像上传成功。"})
        else:
            return Response(serializer.errors, status=400)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key}, status=status.HTTP_200_OK)
