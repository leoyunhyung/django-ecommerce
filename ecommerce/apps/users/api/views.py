# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from ecommerce.apps.users.api.serializers import UserSerializer, LoginSerializer, SignupSerializer, TokenSerializer, \
    WithdrawSerializer
from ecommerce.apps.users.decorators import login_decorator, signup_decorator, me_decorator, withdraw_decorator
from ecommerce.apps.users.models import User
from ecommerce.bases.api.viewsets import GenericViewSet
from ecommerce.utils.api.response import Response
from ecommerce.utils.exception_handlers import CustomBadRequestError


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend,)

    def get_permissions(self):
        if self.action in ['me', 'withdraw']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(**signup_decorator(title=_('유저'), request_body=SignupSerializer))
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                code=201,
                message=_('ok'),
                data=TokenSerializer(instance=instance).data
            )

    @swagger_auto_schema(**login_decorator(title=_('유저'), request_body=LoginSerializer))
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if not user or not user.check_password(password):
            raise CustomBadRequestError('bad request')

        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=TokenSerializer(instance=user).data
        )

    @swagger_auto_schema(**me_decorator(title='유저', serializer=UserSerializer))
    @action(detail=False, methods=['get'])
    def me(self, request):
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=UserSerializer(instance=request.user).data
        )

    @swagger_auto_schema(**withdraw_decorator(title='유저', request_body=WithdrawSerializer))
    @action(detail=False, methods=['delete'])
    def withdraw(self, request):
        user = request.user
        reason = request.data['reason']
        user.set_user_secession(reason=reason)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            code=204,
            message=_('no content'),
        )
