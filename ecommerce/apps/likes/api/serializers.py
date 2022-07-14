# Local
from ecommerce.apps.likes.models import ProductModelLike
from ecommerce.apps.products.api.serializers import ProductModelSerializer
from ecommerce.bases.api.serializers import ModelSerializer


class ProductModelLikeSerializer(ModelSerializer):
    product_model = ProductModelSerializer()

    class Meta:
        model = ProductModelLike
        fields = ('id', 'product_model')
