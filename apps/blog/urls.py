from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views.views import BlogsView, ExtendBlogView, ExtendMoreBlogView, BlogViewSet

urlpatterns = [
    url(r'blog/(?P<pk>\d+)$', BlogsView.as_view(), name="index"),
    url(r'blogs/$', ExtendBlogView.as_view(), name="index"),
    url(r'blogs_ext/(?P<pk>\d+)$', ExtendMoreBlogView.as_view(), name="index"),

]

route = DefaultRouter()
# 可以注册多个,再添加
route.register(r"blogs_view_set", BlogViewSet, base_name="blog")  # 参数1:路由  参数2:视图集  参数3:别名   别名规则: books-list  books-retrieve books-latest books-read  格式: 别名-函数名
urlpatterns += route.urls













