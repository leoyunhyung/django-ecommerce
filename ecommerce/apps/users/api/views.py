# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from ecommerce.apps.users.api.serializers import UserSerializer, LoginSerializer, SignupSerializer, TokenSerializer, \
    WithdrawSerializer, UserAddressCreateSerializer, UserAddressSerializer
from ecommerce.apps.users.decorators import login_decorator, signup_decorator, me_decorator, withdraw_decorator
from ecommerce.apps.users.models import User, UserAddress
from ecommerce.bases.api import mixins
from ecommerce.bases.api.viewsets import GenericViewSet
from ecommerce.utils.api.response import Response
from ecommerce.utils.decorators import token_list_decorator, token_create_decorator, token_patch_decorator, \
    token_destroy_decorator
from ecommerce.utils.exception_handlers import CustomBadRequestError


class UserViewSet(GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = User.objects.all()

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


class UserAddressViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         GenericViewSet):
    serializers = {
        'default': UserAddressSerializer,
        'create': UserAddressCreateSerializer,
        'partial_update': UserAddressCreateSerializer,
    }
    queryset = UserAddress.objects.all().order_by('-created')
    filter_backends = (DjangoFilterBackend,)

    def get_permissions(self):
        if self.action in ['list', 'create', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(**token_list_decorator(title='유저 주소지', serializer=UserAddressSerializer))
    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.filter_queryset(self.get_queryset()).filter(user=user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response(
                status=status.HTTP_200_OK,
                code=200,
                message=_('ok'),
                data=serializer.data
            )

    @swagger_auto_schema(**token_create_decorator(title='유저 주소지'))
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = self.perform_create(serializer)
            return Response(
                status=status.HTTP_201_CREATED,
                code=201,
                message=_('ok'),
                data=UserAddressSerializer(instance=instance).data
            )

    @swagger_auto_schema(**token_patch_decorator(title='유저 주소지'))
    def partial_update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=UserAddressSerializer(instance=instance).data
        )

    @swagger_auto_schema(**token_destroy_decorator(title='유저 주소지'))
    def destroy(self, request, *args, **kwargs):
        user = request.user
        instance = self.get_object()

        if instance.user == user:
            self.perform_destroy(instance)
            # 기본 배송지를 삭제했을 때 아래 코드 실행
            if not UserAddress.objects.filter(is_default=True):
                # 최근 배송지를 기본 배송지로 설정
                try:
                    UserAddress.objects.last().update(is_default=True)
                # 마지막 남은 배송지를 삭제했을 때 이슈 처리
                except:
                    pass
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                code=204,
                message=_('ok'),
            )
        raise PermissionDenied
