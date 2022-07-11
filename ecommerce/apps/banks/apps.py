from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BanksConfig(AppConfig):
    name = "ecommerce.apps.banks"
    verbose_name = _('은행')
