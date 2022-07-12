# Django Rest Framework
from rest_framework import serializers

# Local
from ecommerce.apps.options.api.serializers import OptionGroupSerializer
from ecommerce.apps.products.models import ProductModel
from ecommerce.bases.api.serializers import ModelSerializer


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'banner_image', 'name', 'release_price', 'low_price', 'discount_rate', 'stock')


class ProductModelRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'release_price', 'low_price', 'discount_rate')
