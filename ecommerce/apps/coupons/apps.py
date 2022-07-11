from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CouponsConfig(AppConfig):
    name = "ecommerce.apps.coupons"
    verbose_name = _('쿠폰')
