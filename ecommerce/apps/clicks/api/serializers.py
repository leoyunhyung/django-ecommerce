# Local
from ecommerce.apps.clicks.models import ProductModelClick
from ecommerce.apps.products.api.serializers import ProductModelSerializer
from ecommerce.bases.api.serializers import ModelSerializer


class ProductModelClickSerializer(ModelSerializer):
    product_model = ProductModelSerializer()

    class Meta:
        model = ProductModelClick
        fields = ('id', 'product_model')
