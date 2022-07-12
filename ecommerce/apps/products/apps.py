from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductsConfig(AppConfig):
    name = "ecommerce.apps.products"
    verbose_name = _('상품')

    def ready(self):
        import ecommerce.apps.products.signals
