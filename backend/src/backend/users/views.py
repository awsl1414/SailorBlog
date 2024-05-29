from rest_framework import generics, permissions, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.contrib.auth import get_user_model


from .serializers import UserRegistrationSerializer, AvatarSerializer

User = get_user_model()


@extend_schema(
    summary="用户注册",
    request=UserRegistrationSerializer,
    responses={201: UserRegistrationSerializer},
    description="注册一个新用户，并返回生成的用户信息和身份验证令牌。",
)
class UserRegistrationView(APIView):
    def post(self, requset, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=requset.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            data = {
                "message": "用户注册成功。",
                "user": {
                    "username": user.username,
                    "nickname": user.nickname,
                    "email": user.email,
                },
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    summary="头像上传",
    request=AvatarSerializer,
    responses={200: "头像上传成功。"},
    description="上传用户的头像图片。",
)
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


@extend_schema(
    summary="用户登录",
    request=serializers.Serializer,
    responses={
        200: OpenApiParameter(
            name="token", location=OpenApiParameter.QUERY, description="认证令牌"
        )
    },
)
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response(
            {
                "token": token.key,
                "user": {
                    "user_id": token.user.pk,
                    "username": token.user.username,
                    "nickname": token.user.nickname,
                },
            },
            status=status.HTTP_200_OK,
        )
