from django.conf.urls import url, include
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^', include("apps.blog.urls", namespace="blog")),
    url(r'^', include("apps.users.urls", namespace="users")),
    url(r'^', include("apps.permission.urls", namespace="permission")),
    url(r'^docs/', include_docs_urls(title='API文档'))

]


