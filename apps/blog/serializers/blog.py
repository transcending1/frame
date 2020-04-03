from rest_framework.serializers import Serializer, CharField, DecimalField, IntegerField, PrimaryKeyRelatedField, \
    ListField, DictField, ModelSerializer
from apps.blog.models import Blog


class FansSerializer(Serializer):
    name = CharField()
    price = DecimalField(max_digits=8, decimal_places=2)
    content = CharField()


class ArticleSerializer(Serializer):
    name = CharField()
    price = DecimalField(max_digits=8, decimal_places=2)
    content = CharField()
    fans = FansSerializer(many=True)


# 方式一:通过继承Serializer生成序列化器
class BlogSerializer(Serializer):
    name = CharField(max_length=10, min_length=5, allow_blank=True)
    price = DecimalField(max_digits=8, decimal_places=2)
    category = IntegerField()
    comment = CharField()
    extra_name = CharField()  # 自定义静态属性的返回
    # article = PrimaryKeyRelatedField(read_only=True,many=True)  #常用:仅仅返回外键id 加上many=True返回多个外键id   应用场景:展示列表页面,然后拿着对应的id去访问详情页面
    article = ArticleSerializer(many=True)  # 序列化器嵌套序列化器进行返回(前提:需要写在定义的序列化器前面)


class BlogModelSerializer(ModelSerializer):  #内部已经实现了 create update的方法,直接使用即可,更加方便
    name = CharField(max_length=10, min_length=5, allow_blank=True)  # 由于继承关系,可以通过指定类属性来修改对应的内容

    class Meta:
        model = Blog  # 指定生成字段的模型类,反序列化限制对应的信息通过model层来限制,不在序列化层限制
        fields = ('id', 'name', 'price', 'category', 'comment',
                  'extra_name')  # 直接指定field不能指明内部的属性,可以通过下面的extra来指定修改,可以指定没有的字段,和Serializer类中的内容一致
        # depth = 3  # 指定外键深度
        extra_kwargs = {  # 普遍可以通过这种方式对序列化器内部的字段属性进行更改
            'name': {'min_value': 0, 'required': True},
            'price': {'min_value': 0, 'required': True},
        }

# 序列化使用规范
# BlogSerializer(querryset对象,many=True).data          #序列化器生成对象,然后获取 [{},{},{}..]
# 外键使用两种规定的常用方式


# 反序列化使用规范
# 内部获取request对象
    # self.context['request'].user


# ser = BlogSerializer(data=字典)
# ser.is_valid()  #校验反序列化的合法性   如果使用内置参数:raise_exception=True会抛出异常
# ser.errors  #拿到反序列化的错误信息:指明错误的原因
# ser.validated_data  # 获取反序列化验证后的字段数据
# ser.save()   #序列化器的save方法触发自己定义的create或者update的方法

# 反序列化自定义方法验证
# 1.单一字段验证:方法名固定:  validate_<field_name>
#     def validate_btitle(self, value):
#         if 'django' not in value.lower():
#             raise serializers.ValidationError("图书不是关于Django的")   # 把对应的错误信息放入errors里面,可以通过参数获取
#         return value
# 2.多字段验证:方法名固定,把各种各样的字段放到内部进行验证
#     def validate(self, attrs):
#         bread = attrs['bread']
#         bcomment = attrs['bcomment']
#         if bread < bcomment:
#             raise serializers.ValidationError('阅读量小于评论量')
#         return attrs
# 反序列化的保存,更新操作    ==>  通过序列化器对象的save方法来触发对应的操作
# 1.保存: 定义create函数进行保存的操作     应用场景:可以加入对应的事务处理等操作,可以把核心逻辑放在这里
#     def create(self, validated_data):    # validated_data 代表 校验成功后的数据
#         return BookInfo.objects.create(**validated_data)		# BookInfo为models.py中的一个类 进行实例化就完成了一条记录的添加
# 2.更新:定义update函数进行更新操作
#     序列化器中需要传递更新的对象,保存的时候没有任何关系
#     ser = BlogSerializer(对象,data=字典)
#     def update(self, instance, validated_data):
#         """更新， instance 为要更新的对象实例"""
#         instance.btitle = validated_data.get('btitle', instance.btitle)
#         instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
#         instance.bread = validated_data.get('bread', instance.bread)
#         instance.bcomment = validated_data.get('bcomment', instance.bcomment)
#         instance.save()    #保存到数据库
#         return instance
