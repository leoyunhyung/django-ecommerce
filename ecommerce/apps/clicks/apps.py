from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClicksConfig(AppConfig):
    name = "ecommerce.apps.clicks"
    verbose_name = _('클릭')
