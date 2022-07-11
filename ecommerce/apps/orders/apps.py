from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrdersConfig(AppConfig):
    name = "ecommerce.apps.orders"
    verbose_name = _('주문')
