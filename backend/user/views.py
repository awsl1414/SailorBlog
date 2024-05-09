from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(["POST"])
@permission_classes([])
@extend_schema(
    request=UserSerializer,
    responses={201: UserSerializer},
    description="用户注册，包含头像上传。",
)
def register(request):
    parser_classes = (MultiPartParser, FormParser)
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
