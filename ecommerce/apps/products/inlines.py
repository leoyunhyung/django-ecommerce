from ecommerce.apps.options.models import OptionGroup
from ecommerce.bases.inlines import TabularInline

from ecommerce.apps.products.models import ProductOption


class ProductOptionInline(TabularInline):
    model = ProductOption
    fk_name = 'product'
    fields = ('option',)
    extra = 1

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return True
