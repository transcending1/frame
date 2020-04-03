from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status
from django.db import DatabaseError


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    print("kO")
    if response is None:  # 数据库异常自定义捕获
        view = context['view']
        if isinstance(exc, DatabaseError):  # 捕获数据库异常然后返回给前端处理
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': str(exc)}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
