# Django
from django.contrib import admin

# Local
from ecommerce.apps.orders.models import OrderGroup, Order
from ecommerce.apps.products.inlines import ProductOptionInline
from ecommerce.apps.products.models import ProductModel, Product
from ecommerce.bases.admin import Admin


@admin.register(OrderGroup)
class OrderGroupAdmin(Admin):
    list_display = ('user', 'delivery', 'payment_type', 'total_price', 'discount_price', 'payment_price', 'is_agreement')
    search_fields = ('user__email', 'payment_type', 'discount_price', 'total_price')
    ordering = ('-created',)
    list_filter = ()


@admin.register(Order)
class OrderAdmin(Admin):
    list_display = ('user', 'order_group', 'product', 'cart', 'product_model', 'code', 'size', 'price')
    search_fields = ('user__email', 'order_group__id', 'product__id', 'cart__id', 'product_model__name', 'code', 'size', 'price')
    ordering = ('-created',)
    list_filter = ()
