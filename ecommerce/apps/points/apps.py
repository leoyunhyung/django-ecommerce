from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PointsConfig(AppConfig):
    name = "ecommerce.apps.points"
    verbose_name = _('포인트')
