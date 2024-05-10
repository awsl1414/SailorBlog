from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.authtoken.models import Token


UserInfo = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
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
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError("密码不匹配。")
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = UserInfo.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            nickname=validated_data["nickname"],
            bio=validated_data["bio"],
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
