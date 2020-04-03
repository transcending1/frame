from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.permission.serializers.groups import GroupSerializer
from apps.permission.serializers.permission import PerssionsSerialzier, ContentTypeSerialzier
from utils.pagination import StandardPageNumberPagination


class PermissionsView(ModelViewSet):
    serializer_class = PerssionsSerialzier
    queryset = Permission.objects.all()
    pagination_class = StandardPageNumberPagination

    # 父类中没有权限类型表的操作，需要自己封装方法
    @action(methods=["get"],detail=False)
    def content_type(self, request):
        """
            获取权限类型
        :param request:
        :return:
        """
        # 1、获取权限类型的所有数据
        data = ContentType.objects.all()

        # 2、序列化返回权限类型  self.get_serializer() 获取serializer_class属性所指定的序列器对象
        ser = ContentTypeSerialzier(data, many=True)  # 初始化生成序列化器对象

        return Response(ser.data)




class GroupView(ModelViewSet):
    # 父类方法需要调用序列化器
    serializer_class = GroupSerializer
    # 视图集属性
    queryset = Group.objects.all()
    # 分页属性
    pagination_class = StandardPageNumberPagination


    @action(methods=['get'],detail=False)  # methods指定方法所对应的请求方式 detail指定在生成的路径中是否需要正则匹配
    def simple(self, request):
        """
            获取权限数据
        :param request:
        :return:
        """
        # 1、查询权限表
        data = Permission.objects.all()
        # 2、返回权限数据

        ser = PerssionsSerialzier(data, many=True)

        return Response(ser.data)
