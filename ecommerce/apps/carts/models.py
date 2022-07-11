# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class Cart(Model):
    user = models.ForeignKey('users.User',
                             verbose_name=_('유저'),
                             on_delete=models.CASCADE,
                             related_name='carts')
    product = models.ForeignKey('products.Product',
                                verbose_name=_('상품'),
                                on_delete=models.CASCADE,
                                related_name='carts')

    quantity = models.IntegerField(_('수량'), default=1)
    is_purchased = models.BooleanField(_('구매'), default=False)

    class Meta:
        verbose_name = verbose_name_plural = _('카트')
