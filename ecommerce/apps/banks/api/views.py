# Django
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework.permissions import IsAuthenticated, AllowAny

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from ecommerce.apps.banks.api.serializers import BankAccountSerializer, BankAccountCreateSerializer
from ecommerce.apps.banks.models import BankAccount
from ecommerce.bases.api import mixins
from ecommerce.bases.api.viewsets import GenericViewSet
from ecommerce.utils.decorators import token_create_decorator, token_list_decorator


class BankAccountViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         GenericViewSet):
    serializers = {
        'default': BankAccountSerializer,
        'create': BankAccountCreateSerializer,
    }
    filter_backends = (DjangoFilterBackend,)
    queryset = BankAccount.objects.all().order_by('-created')

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(**token_list_decorator(title=_('은행 계좌'), serializer=BankAccountSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(**token_create_decorator(title='은행 계좌'))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
