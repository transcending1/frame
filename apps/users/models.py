from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from rest_framework_jwt.settings import api_settings

from exlib.sql_extension import BaseModel


class User(AbstractUser):
    """用户模型类"""

    MALE, FEMALE, UNKNOWN = 1, 2, 0

    GENDERS = ((MALE, '男性'), (FEMALE, '女性'), (UNKNOWN, '保密'))

    nick = models.CharField('nick', max_length=64, help_text="昵称")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号', help_text="手机号")
    avatar = models.CharField('头像', max_length=256, default='', help_text="头像")
    gender = models.SmallIntegerField('性别', default=UNKNOWN, help_text="性别")

    coins = models.IntegerField("剩余书币", default=0, help_text="剩余书币")

    def gen_jwt_token(self):
        '''
            用户登录注册的时候生成jwt的token值
        '''

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(self)  # user为一个用户对象
        return jwt_encode_handler(payload)  # 生成token








