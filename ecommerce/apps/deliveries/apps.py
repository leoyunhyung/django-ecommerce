from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DeliveriesConfig(AppConfig):
    name = "ecommerce.apps.deliveries"
    verbose_name = _('배송 정보')
