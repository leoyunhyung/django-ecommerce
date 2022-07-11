from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LikesConfig(AppConfig):
    name = "ecommerce.apps.likes"
    verbose_name = _('찜')
