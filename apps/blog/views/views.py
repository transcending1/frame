from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_extensions.cache.decorators import cache_response

from apps.blog.models import Blog
from apps.blog.serializers.blog import BlogModelSerializer
from utils.pagination import StandardPageNumberPagination


class BlogsView(GenericAPIView):
    # 指定查询集数据
    queryset = Blog.objects.all()  # 指定查询集
    serializer_class = BlogModelSerializer  # 当前类视图使用的序列化器

    def get(self, request, pk):
        print(pk)
        blog = self.get_object()  # 根据pk来获取对象,如果没有找到的话直接返回404
        blogs = self.get_queryset()  # 获取查询集     ==>可以对对应的方法进行重写,灵活获取各种querryset对象
        ser = self.get_serializer(blogs, many=True)  # 得到序列化器对象   ==>可以对对应方法进行重写,灵活获取各种序列化器对象
        return Response(ser.data)


class ExtendBlogView(GenericAPIView, ListModelMixin):
    queryset = Blog.objects.all()  # 指定查询集
    serializer_class = BlogModelSerializer  # 当前类视图使用的序列化器

    def get(self, request):
        return self.list(request)


class ExtendMoreBlogView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


from rest_framework.viewsets import ModelViewSet


class BlogViewSet(ModelViewSet):
    """
        返回所有博客的信息.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    # filter_fields = ('name',)  # 过滤器的使用,相当于GET请求传递特定参数进行过滤. 大幅度简化了相关操作
    # 如果需要模糊搜索的话也可以支持(拓展:可以自定义search机制,插入es也可以)  https://www.django-rest-framework.org/api-guide/filtering/
    # filter_backends = [OrderingFilter]  # 排序操作的使用
    # ordering_fields = ('create_time',)  # 排序操作
    pagination_class = StandardPageNumberPagination  # 分页器的指定

    permission_classes = (IsAuthenticated,)  # 全局视图的认证方式



    def get_queryset(self):
        '''
        可以根据请求参数自定制querryset
        :return:
        '''
        return self.queryset

    def get_permissions(self):
        '''
            具体视图的权限控制机制,权限精确到类中的每一个函数
        '''
        if self.action == "create":  # 指定 latest 函数
            return [IsAuthenticated()]  # 通过认证的用户
        else:
            return [AllowAny()]  # 所有用户

    def get_serializer_class(self):
        '''
            自定义序列化器,重写 这样通过 self.get_serializer(blog)  可以得到自己想要的序列化器对象,更灵活,覆盖类属性
        '''
        if self.action == "latest":  # 通过self.action可以获取对应的action指定的方法
            return BlogModelSerializer
        else:
            return BlogModelSerializer

    @action(methods=["get"], detail=False)  # 只要加上了装饰器就可以根据self.action来区别不同的视图
    def latest(self, request):
        '''
            最新博客的信息获取
        '''
        self.get_queryset()
        blog = Blog.objects.latest("id")
        serializer = self.get_serializer(blog)
        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def how(self, request, pk):
        '''
            最新博客的信息获取
        '''
        print(pk)
        blog = Blog.objects.latest("id")
        serializer = self.get_serializer(blog)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):  # 复杂的情况下重写视图集下面的各种方法
        return super().create(request)

    @cache_response(timeout=60 * 60)
    def list(self, request, *args, **kwargs):
        return super().list(request)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, kwargs.get("pk"))

    def update(self, request, *args, **kwargs):
        return super().update(request, kwargs.get("pk"))

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, kwargs.get("pk"))
