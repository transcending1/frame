from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.users.models import User
from apps.users.serializers.users import UserModelSerializer, UserLoginSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class UsersViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin,GenericViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        return [AllowAny()] if self.action == "login" else [IsAuthenticated()]

    def get_serializer_class(self):
        return UserLoginSerializer if self.action == "login" else UserModelSerializer

    @action(methods=["post"], detail=False)
    def login(self, request):
        '''
            用户登录
        '''
        ser = UserLoginSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        return Response(data=ser.validated_data, status=200)
