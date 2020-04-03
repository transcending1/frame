from rest_framework.routers import DefaultRouter

from apps.users.views.login import UsersViewSet

urlpatterns = [

]

route = DefaultRouter()
# 可以注册多个,再添加
route.register(r"users", UsersViewSet, base_name="users")  # 参数1:路由  参数2:视图集  参数3:别名   别名规则: books-list  books-retrieve books-latest books-read  格式: 别名-函数名
urlpatterns += route.urls
