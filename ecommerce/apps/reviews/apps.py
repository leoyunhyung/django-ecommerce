from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReviewsConfig(AppConfig):
    name = "ecommerce.apps.reviews"
    verbose_name = _('리뷰')
