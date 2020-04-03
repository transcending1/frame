from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class UserModelSerializer(ModelSerializer):  # 内部已经实现了 create update的方法,直接使用即可,更加方便
    token = CharField(read_only=True)

    class Meta:
        model = User  # 指定生成字段的模型类,反序列化限制对应的信息通过model层来限制,不在序列化层限制
        fields = ('id', 'username', 'password', 'token','user_permissions','groups')
        extra_kwargs = {  # 可以通过这种方式对序列化器内部的字段属性进行更改
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        '''
            用户注册
        '''
        user = super().create(validated_data)

        # 调用django的认证系统加密密码
        user.set_password(validated_data['password'])
        user.save()

        # 手动为用户生成jwt token
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)  # user为一个用户对象
        token = jwt_encode_handler(payload)  # 生成token

        # 把token保存到user对象中,随着返回值返回给前端,Restful风格自动会返回
        user.token = token
        return user


class UserLoginSerializer(ModelSerializer):
    token = CharField(read_only=True)
    username = CharField(write_only=True)

    class Meta:
        model = User  # 指定生成字段的模型类,反序列化限制对应的信息通过model层来限制,不在序列化层限制
        fields = ('username', 'password', 'token')
        extra_kwargs = {  # 可以通过这种方式对序列化器内部的字段属性进行更改
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        '''
            用户登录行为验证
        '''
        username = attrs["username"]
        password = attrs["password"]
        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError("没有对应的用户名")
        if not user.check_password(password):
            raise ValidationError("用户密码不正确")
        # 手动为用户生成jwt token
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)  # user为一个用户对象
        token = jwt_encode_handler(payload)  # 生成token

        # 把token保存到user对象中,随着返回值返回给前端,Restful风格自动会返回
        attrs["token"] = token
        attrs["id"] = user.id
        attrs.pop("password")
        return attrs
