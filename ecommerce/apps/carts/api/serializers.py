# Local
from ecommerce.apps.carts.models import Cart
from ecommerce.apps.products.api.serializers import ProductSerializer
from ecommerce.bases.api.serializers import ModelSerializer


class CartSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ('id', 'product',)


class CartCreateSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('product',)

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        validated_data['user'] = user
        cart = Cart.objects.create(**validated_data)
        return cart
