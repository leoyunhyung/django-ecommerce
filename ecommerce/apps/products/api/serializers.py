# Local
from ecommerce.apps.products.models import ProductModel, Product
from ecommerce.bases.api.serializers import ModelSerializer


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'banner_image', 'name', 'release_price', 'low_price', 'discount_rate', 'stocks')


class ProductModelRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'release_price', 'low_price', 'discount_rate')


class ProductModelOrderSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'banner_image', 'name')


class ProductSerializer(ModelSerializer):
    product_model = ProductModelOrderSerializer()

    class Meta:
        model = Product
        fields = ('id', 'product_model', 'code', 'price', 'size')
