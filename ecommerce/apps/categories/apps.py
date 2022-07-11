from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CategoriesConfig(AppConfig):
    name = "ecommerce.apps.categories"
    verbose_name = _('카테고리')
