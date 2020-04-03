from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.serializers.users import UserModelSerializer, UserLoginSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @action(methods=["post"], detail=False)
    def login(self, request):
        '''
            用户登录
        '''
        ser = UserLoginSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        return Response(data=ser.validated_data, status=200)
