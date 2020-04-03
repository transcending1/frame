'''
    此文件用来拓展用户的鉴权机制
'''
from django.contrib.auth.backends import ModelBackend

from apps.users.models import User


def jwt_response_payload_handler(token, user=None, request=None):
    '''
        drf中的jwt登录成功后自定义返回的信息
    '''
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }


def get_user_by_account(username):
    '''

    '''
    return User.objects.filter(username=username).first()


class UsernameMobileAuthBackend(ModelBackend):
    '''
        在这里可以根据前端的请求内容得到对应的用户对象
    '''
    def authenticate(self, request, username=None, password=None, **kwargs):  # 定义 authenticate 函数,里面写主逻辑
        # 会自动根据用户对象查询出username , password 的信息
        user = get_user_by_account(username)
        if user is not None and user.check_password(password):
            # 验证成功返回对象,验证失败什么都不用做
            return user
