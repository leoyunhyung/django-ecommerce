from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ImagesConfig(AppConfig):
    name = "ecommerce.apps.images"
    verbose_name = _('이미지')
