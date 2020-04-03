from rest_framework.routers import DefaultRouter
from apps.permission.views.permission import PermissionsView, GroupView

urlpatterns = [

]

route = DefaultRouter()
# 可以注册多个,再添加
route.register(r"permissions", PermissionsView, base_name="permissions")
route.register(r"groups", GroupView, base_name="groups")
urlpatterns += route.urls
