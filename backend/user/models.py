from django.db import models
from django.contrib.auth.models import AbstractUser

# 延迟国际化（i18n）翻译功能
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    nickname = models.CharField(
        _("nickname"), max_length=150, blank=True, help_text=_("昵称")
    )
    avatar = models.ImageField(
        _("avatar"), upload_to="avatars/", blank=True, null=True, help_text=_("头像")
    )
    bio = models.TextField(
        _("bio"), blank=True, max_length=500, help_text=_("个人简介")
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"
        verbose_name = _("用户")
        verbose_name_plural = _("用户")
