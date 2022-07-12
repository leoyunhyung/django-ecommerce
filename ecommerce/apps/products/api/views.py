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
from ecommerce.apps.products.api.serializers import ProductModelSerializer, ProductModelRetrieveSerializer
from ecommerce.apps.products.models import ProductModel
from ecommerce.bases.api import mixins
from ecommerce.bases.api.viewsets import GenericViewSet
from ecommerce.utils.decorators import list_decorator, retrieve_decorator


class ProductModelViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          GenericViewSet):
    serializers = {
        'default': ProductModelSerializer,
        'retrieve': ProductModelRetrieveSerializer,
                   }
    queryset = ProductModel.objects.all().order_by('-created')
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**list_decorator(title=_('상품 모델'), serializer=ProductModelSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(**retrieve_decorator(title=_('상품 모델'), serializer=ProductModelRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)
