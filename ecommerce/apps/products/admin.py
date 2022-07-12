# Django
from django.contrib import admin

# Local
from ecommerce.apps.products.inlines import ProductOptionInline
from ecommerce.apps.products.models import ProductModel, Product
from ecommerce.bases.admin import Admin


@admin.register(ProductModel)
class ProductModelAdmin(Admin):
    list_display = ('category', 'banner_image', 'name', 'release_price', 'low_price', 'discount_rate', 'stock')
    search_fields = ('category__category_group__name', 'category__name', 'name', 'release_price', 'low_price', 'discount_rate', 'stock')
    ordering = ('-created',)
    list_filter = ()

    fieldsets = (
        ("Fk", {"fields": ('category', 'banner_image')}),
        ("Main", {"fields": ('id', 'name', 'release_price')}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    add_fieldsets = (
        ("Fk", {"fields": ('category', 'banner_image')}),
        ("Main", {"fields": ('name', 'release_price')}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    readonly_fields = ("created", "modified")


@admin.register(Product)
class ProductAdmin(Admin):
    list_display = ('product_model', 'price', 'code')
    search_fields = ('product_model__name', 'price', 'code')
    ordering = ('-created',)
    list_filter = ()

    fieldsets = (
        ("Fk", {"fields": ('product_model',)}),
        ("Main", {"fields": ('id', 'price', 'code')}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    add_fieldsets = (
        ("Fk", {"fields": ('product_model',)}),
        ("Main", {"fields": ('price', 'code')}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    readonly_fields = ("created", "modified")

    inlines = (ProductOptionInline,)
