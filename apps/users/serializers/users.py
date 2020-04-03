from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class UserModelSerializer(ModelSerializer):  # 内部已经实现了 create update的方法,直接使用即可,更加方便
    token = CharField(read_only=True)

    class Meta:
        model = User  # 指定生成字段的模型类,反序列化限制对应的信息通过model层来限制,不在序列化层限制
        fields = ('id', 'nick', 'token')


    def create(self, validated_data):
        '''
            用户注册
        '''
        user = User(**validated_data)

        # 把token保存到user对象中,随着返回值返回给前端,Restful风格自动会返回
        user.token = user.gen_jwt_token()
        return user


class UserLoginSerializer(ModelSerializer):
    token = CharField(read_only=True)
    code = CharField(write_only=True, required=True)

    class Meta:
        model = User  # 指定生成字段的模型类,反序列化限制对应的信息通过model层来限制,不在序列化层限制
        fields = ('mobile', 'token', 'code')
        extra_kwargs = {  # 可以通过这种方式对序列化器内部的字段属性进行更改
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        '''
            用户登录行为验证
        '''

        user = User.objects.filter(mobile=attrs["mobile"]).first()
        if not user:
            user = User(username=attrs["mobile"],mobile = attrs["mobile"],nick="用户{}".format(attrs["mobile"])).save()
        if attrs['code'] != "111":  #redis里面获取值,然后判断是否相等
            raise ValidationError("验证码不正确")

        # 把token保存到user对象中,随着返回值返回给前端,Restful风格自动会返回
        attrs["token"] = user.gen_jwt_token()
        attrs["id"] = user.id
        return attrs
