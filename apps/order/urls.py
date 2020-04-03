from rest_framework.routers import DefaultRouter
from apps.users.views.login import UsersViewSet
from apps.article.views import views

urlpatterns = [

]

route = DefaultRouter()
# 可以注册多个,再添加
route.register(r"books", views.BooksViewSet, base_name="书籍")
route.register(r"chapters", views.ChaptersViewSet, base_name="章节")
route.register(r"categories", views.CategoriesViewSet, base_name="书籍类型")
urlpatterns += route.urls
