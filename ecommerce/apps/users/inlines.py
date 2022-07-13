from ecommerce.apps.points.models import Point
from ecommerce.bases.inlines import TabularInline


class PointInline(TabularInline):
    model = Point
    fk_name = 'user'
    fields = ('name', 'description', 'discount_price')
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return True
