from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryChoices(models.TextChoices):
    BACKEND = "Backend", "后端"
    FRONTEND = "Frontend", "前端"
    LIFESTYLE = "Lifestyle", "生活"

    def __str__(self):
        return self.name


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
