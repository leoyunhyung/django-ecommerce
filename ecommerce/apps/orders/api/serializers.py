# Python
from collections import OrderedDict

# Django Rest Framework
from rest_framework import serializers

# Local
from ecommerce.apps.orders.models import Order, OrderGroup
from ecommerce.bases.api.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('product_model', 'product', 'cart', 'code', 'size', 'price')

    def to_representation(self, instance):
        result = super(OrderSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class OrderGroupSerializer(ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = OrderGroup
        fields = ('id', 'delivery', 'payment_type', 'total_price', 'discount_price', 'payment_price', 'is_agreement', 'orders')

    def get_orders(self, obj):
        return OrderSerializer(instance=obj.orders, read_only=True, many=True).data


class OrderGroupCreateSerializer(ModelSerializer):
    product = serializers.IntegerField(required=False)
    cart = serializers.IntegerField(required=False)
    point = serializers.IntegerField(required=False)

    class Meta:
        model = OrderGroup
        fields = ('product', 'cart', 'point', 'payment_type')
