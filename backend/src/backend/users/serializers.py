from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.authtoken.models import Token


UserInfo = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True, required=True, help_text="确认密码"
    )

    class Meta:
        model = UserInfo
        fields = (
            "username",
            "email",
            "password",
            "confirm_password",
            "nickname",
            "bio",
        )
        extra_kwargs = {
            "password": {"write_only": True, "help_text": "密码"},
            "email": {"required": True, "allow_blank": False, "help_text": "邮箱"},
        }

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError("密码不匹配。")

        # TODO 增加更多的验证规则，例如用户名是否已存在，邮箱是否已注册等
        # if len(password) < 8:
        #     raise serializers.ValidationError("密码长度至少为8个字符。")
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = UserInfo(
            username=validated_data["username"],
            email=validated_data["email"],
            nickname=validated_data.get("nickname", ""),
            bio=validated_data.get("bio", ""),
        )
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("avatar",)

    def save(self, **kwargs):
        user = self.context["request"].user
        user.avatar = self.validated_data["avatar"]
        user.save()
        return user
