# Django
from django.contrib import admin

# Local
from ecommerce.apps.carts.models import Cart
from ecommerce.bases.admin import Admin


@admin.register(Cart)
class CartAdmin(Admin):
    list_display = ('user', 'product__product_model__name', 'product__code', 'product__size', 'product__price', 'is_purchased')
    search_fields = ('user__email', 'product__product_model__name', 'product__code', 'product__size', 'product__price')
    ordering = ('-created',)
    list_filter = ()
