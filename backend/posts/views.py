from django.shortcuts import render
from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema

from .models import Post
from .serializers import PostSerializer


@extend_schema(
    summary="获取所有文章和创建文章",
    request=PostSerializer,
    responses={200: PostSerializer},
)
# 获取所有文章和创建文章
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # 权限控制：未登录用户只能读取，登录用户可以创建
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(
    summary="获取单个文章、修改文章和删除文章",
    request=PostSerializer,
    responses={200: PostSerializer},
)
# 获取单个文章、修改文章和删除文章
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # 权限控制：未登录用户只能读取，登录用户可以修改和删除
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
