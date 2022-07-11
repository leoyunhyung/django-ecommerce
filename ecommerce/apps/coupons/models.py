# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class Coupon(Model):
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='coupons')
    name = models.CharField(_('이름'), max_length=100)
    description = models.CharField(_('설명'), max_length=100)
    discount_price = models.IntegerField(_('할인 금액'), null=True, blank=True)
    discount_rate = models.IntegerField(_('할인율'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('쿠폰')
