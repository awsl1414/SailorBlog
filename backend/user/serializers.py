from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import os

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "confirm_password",
            "nickname",
            "avatar",
            "bio",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs.pop("confirm_password"):
            raise ValidationError("两次输入的密码不匹配。")

        # 文件大小验证示例：
        avatar = attrs.get("avatar")
        if avatar and avatar.size > 5 * 1024 * 1024:  # 限制大小为5MB
            raise ValidationError("头像文件大小不能超过5MB。")

        # 文件类型验证示例：
        if avatar and os.path.splitext(avatar.name)[1] not in [".jpg", ".jpeg", ".png"]:
            raise ValidationError("不支持的文件类型。")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            nickname=validated_data.get("nickname", ""),
            bio=validated_data.get("bio", ""),
        )
        user.set_password(validated_data["password"])
        user.avatar = validated_data.get("avatar")
        user.save()

        return user
