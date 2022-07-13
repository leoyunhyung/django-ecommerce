# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from ecommerce.apps.carts.api.serializers import CartSerializer, CartCreateSerializer
from ecommerce.apps.carts.models import Cart
from ecommerce.bases.api import mixins
from ecommerce.bases.api.viewsets import GenericViewSet
from ecommerce.utils.api.response import Response
from ecommerce.utils.decorators import token_list_decorator, token_create_decorator, token_destroy_decorator


class CartViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  GenericViewSet):
    serializers = {
        'default': CartSerializer,
        'create': CartCreateSerializer
    }
    queryset = Cart.objects.filter(is_purchased=False).order_by('-created')
    filter_backends = (DjangoFilterBackend,)

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(**token_list_decorator(title='카트', serializer=CartSerializer))
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

    @swagger_auto_schema(**token_create_decorator(title='카트'))
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = self.perform_create(serializer)
            return Response(
                status=status.HTTP_201_CREATED,
                code=201,
                message=_('ok'),
                data=CartSerializer(instance=instance).data
            )

    @swagger_auto_schema(**token_destroy_decorator(title='카트'))
    def destroy(self, request, *args, **kwargs):
        user = request.user
        instance = self.get_object()
        if instance.user == user:
            self.perform_destroy(instance)
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                code=204,
                message=_('ok'),
            )
        raise PermissionDenied
