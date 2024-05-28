from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        # fields = "__all__"
        fields = (
            "id",
            "author",
            "title",
            "body",
            "category",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("author", "created_at", "updated_at")
