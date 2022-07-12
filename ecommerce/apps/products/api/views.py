# Django
import django_filters
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from ecommerce.apps.products.api.serializers import ProductModelSerializer, ProductModelRetrieveSerializer, \
    ProductSerializer
from ecommerce.apps.products.decorators import product_list_decorator
from ecommerce.apps.products.models import ProductModel, Product
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
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = ProductModel.objects.all().order_by('-created')
        return queryset

    @swagger_auto_schema(**list_decorator(title=_('상품 모델'), serializer=ProductModelSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(**retrieve_decorator(title=_('상품 모델'), serializer=ProductModelRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)


class ArrayFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            values = value.split(',')
            return qs.filter(**{'%s__%s' % (self.field_name, self.lookup_expr): values}).distinct()
        return qs


class ProductFilterSet(django_filters.FilterSet):
    size = ArrayFilter(field_name='product_options__option__name', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['size']


class ProductViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    serializers = {
        'default': ProductSerializer,
    }
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProductFilterSet

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = Product.objects.filter(product_model=self.kwargs['product_model_pk']).order_by('-created')
        return queryset

    @swagger_auto_schema(**product_list_decorator(title=_('상품 모델'), serializer=ProductSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
