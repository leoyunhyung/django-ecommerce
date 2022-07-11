# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class OrderGroup(Model):
    user = models.ForeignKey('users.User',
                             verbose_name=_('유저'),
                             on_delete=models.CASCADE,
                             related_name='order_groups')
    total_price = models.IntegerField(_('총 가격'), default=0)

    class Meta:
        verbose_name = verbose_name_plural = _('주문 그룹')


class Order(Model):
    user = models.ForeignKey('users.User',
                             verbose_name=_('유저'),
                             on_delete=models.CASCADE,
                             related_name='orders')
    order_group = models.ForeignKey('OrderGroup',
                                    verbose_name=_('주문 그룹'),
                                    on_delete=models.CASCADE,
                                    related_name='orders')
    product = models.ForeignKey('products.Product',
                                verbose_name=_('상품'),
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='orders')
    cart = models.OneToOneField('carts.Cart',
                                verbose_name=_('카트'),
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='orders')
    product_model = models.JSONField(_('상품 모델'), null=True, blank=True)
    quantity = models.IntegerField(_('수량'), default=1, null=True, blank=True)
    price = models.IntegerField(_('가격'), default=0)

    class Meta:
        verbose_name = verbose_name_plural = _('주문')
