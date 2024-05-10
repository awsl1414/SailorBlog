from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, extend_schema
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser


from .serializers import UserRegistrationSerializer, AvatarSerializer

User = get_user_model()


@extend_schema(
    request=UserRegistrationSerializer, responses={201: UserRegistrationSerializer}
)
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "avatar": {
                    "type": "string",
                    "format": "binary",
                    "description": "上传的头像图片",
                }
            },
        }
    },
    responses={200: AvatarSerializer},
)
class AvatarUploadView(generics.UpdateAPIView):
    serializer_class = AvatarSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "头像上传成功。"})
        else:
            return Response(serializer.errors, status=400)
