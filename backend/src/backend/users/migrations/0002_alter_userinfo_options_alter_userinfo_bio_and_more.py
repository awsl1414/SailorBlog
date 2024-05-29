# Generated by Django 5.0.6 on 2024-05-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userinfo",
            options={"verbose_name": "用户", "verbose_name_plural": "用户"},
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="bio",
            field=models.CharField(
                blank=True, help_text="个人简介", max_length=500, verbose_name="bio"
            ),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="nickname",
            field=models.CharField(
                blank=True,
                help_text="昵称",
                max_length=150,
                unique=True,
                verbose_name="nickname",
            ),
        ),
        migrations.AddIndex(
            model_name="userinfo",
            index=models.Index(fields=["username"], name="username_idx"),
        ),
        migrations.AddIndex(
            model_name="userinfo",
            index=models.Index(fields=["nickname"], name="nickname_idx"),
        ),
        migrations.AddIndex(
            model_name="userinfo",
            index=models.Index(fields=["avatar"], name="avatar_idx"),
        ),
        migrations.AlterModelTable(
            name="userinfo",
            table="user_info",
        ),
    ]