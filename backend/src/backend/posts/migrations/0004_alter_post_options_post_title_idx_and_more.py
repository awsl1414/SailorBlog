# Generated by Django 5.0.6 on 2024-05-29 08:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_rename_categroy_post_category"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "文章", "verbose_name_plural": "文章"},
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["title"], name="title_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["created_at"], name="created_at_idx"),
        ),
        migrations.AlterModelTable(
            name="post",
            table="post",
        ),
    ]
