# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class Image(Model):
    image = models.ImageField(_('이미지'))
    url = models.URLField(_('이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('이미지')
