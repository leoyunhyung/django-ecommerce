# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class Point(Model):
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='points')
    name = models.CharField(_('이름'), max_length=100, null=True, blank=True)
    description = models.CharField(_('설명'), max_length=100, null=True, blank=True)
    discount_price = models.IntegerField(_('할인 금액'))

    class Meta:
        verbose_name = verbose_name_plural = _('포인트')
