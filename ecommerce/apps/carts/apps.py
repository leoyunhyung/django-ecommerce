from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CartsConfig(AppConfig):
    name = "ecommerce.apps.carts"
    verbose_name = _('카트')
