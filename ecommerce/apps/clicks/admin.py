# Django
from django.contrib import admin

# Local
from ecommerce.apps.clicks.models import ProductModelClick
from ecommerce.bases.admin import Admin


@admin.register(ProductModelClick)
class ProductModelClickAdmin(Admin):
    list_display = ('user', 'product_model__name')
    search_fields = ('user__email', 'product_model__name')
    ordering = ('-created',)
    list_filter = ()

    fieldsets = (
        ("Fk", {"fields": ('user',)}),
        ("Main", {"fields": ('id', 'product_model')}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    add_fieldsets = (
        ("Fk", {"fields": ('user',)}),
        ("Main", {"fields": ('product_model',)}),
        ("Date", {"fields": ('created', 'modified',)}),
    )

    readonly_fields = ("created", "modified")
