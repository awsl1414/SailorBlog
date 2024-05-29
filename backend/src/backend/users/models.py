from django.db import models
from django.contrib.auth.models import AbstractUser

# 延迟国际化（i18n）翻译功能
from django.utils.translation import gettext_lazy as _


class UserInfo(AbstractUser):
    nickname = models.CharField(
        _("nickname"), max_length=150, blank=True, unique=True, help_text=_("昵称")
    )
    avatar = models.ImageField(
        _("avatar"), upload_to="avatars/", blank=True, null=True, help_text=_("头像")
    )
    bio = models.CharField(
        _("bio"), blank=True, max_length=500, help_text=_("个人简介")
    )

    def __str__(self):
        # 优先展示昵称，否则展示用户名
        return self.nickname if self.nickname else self.username

    class Meta:
        db_table = "user_info"  # 表名使用小写和下划线风格，更符合数据库表名的惯例
        verbose_name = _("用户")
        verbose_name_plural = _("用户")

        # 添加索引
        indexes = [
            models.Index(fields=["username"], name="username_idx"),
            models.Index(fields=["nickname"], name="nickname_idx"),
            models.Index(fields=["avatar"], name="avatar_idx"),
        ]
