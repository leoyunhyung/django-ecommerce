# Django
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from ecommerce.apps.orders.api.serializers import OrderGroupSerializer, OrderGroupCreateSerializer
from ecommerce.apps.orders.models import OrderGroup
from ecommerce.bases.api import mixins
from ecommerce.bases.api.viewsets import GenericViewSet
from ecommerce.utils.api.response import Response
from ecommerce.utils.decorators import token_create_decorator, token_list_decorator
from ecommerce.utils.exception_handlers import CustomBadRequestError


class OrderGroupViewSet(mixins.ListModelMixin,
                        GenericViewSet):
    serializers = {
        'default': OrderGroupSerializer,
        'create': OrderGroupCreateSerializer,
    }
    filter_backends = (DjangoFilterBackend,)
    queryset = OrderGroup.objects.all().prefetch_related('orders').order_by('-created')

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(**token_list_decorator(title=_('주문 그룹'), serializer=OrderGroupSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(**token_create_decorator(title='주문 그룹'))
    def create(self, request, *args, **kwargs):
        user = request.user
        product = request.data.get('product', None)
        cart = request.data.get('cart', None)
        point = request.data.get('point', 0)
        payment_type = request.data['payment_type']

        if point > user.point:
            raise CustomBadRequestError('bad request')

        instance = user.set_order_group(cart, product, point, payment_type)

        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=OrderGroupSerializer(instance=instance).data
        )
