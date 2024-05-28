from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryChoices(models.TextChoices):
    BACKEND = "Backend", "后端"
    FRONTEND = "Frontend", "前端"
    LIFESTYLE = "Lifestyle", "生活"

    def __str__(self):
        return self.label  # 更改为 label，便于显示友好名称


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(
        max_length=50, choices=CategoryChoices.choices, default=CategoryChoices.BACKEND
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_excerpt(self, char_limit=200):
        """
        获取文章摘要，默认限制 200 个字符
        """
        return (
            self.body[:char_limit] + "..." if len(self.body) > char_limit else self.body
        )

    class Meta:
        db_table = "post"
        verbose_name = "文章"
        verbose_name_plural = "文章"
        indexes = [
            models.Index(fields=["title"], name="title_idx"),
            models.Index(fields=["created_at"], name="created_at_idx"),
        ]
