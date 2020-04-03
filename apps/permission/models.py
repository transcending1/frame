from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    """用户模型类"""
    mobile = CharField(max_length=11, null=True, blank=True, verbose_name='手机号',help_text="手机号")
