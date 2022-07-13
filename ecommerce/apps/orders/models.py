# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model
from ecommerce.modules.choices import PAYMENT_TYPE_CHOICES


class OrderGroup(Model):
    user = models.ForeignKey('users.User',
                             verbose_name=_('유저'),
                             on_delete=models.CASCADE,
                             related_name='order_groups')
    delivery = models.OneToOneField('deliveries.Delivery',
                                    verbose_name=_('배송 정보'),
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    related_name='order_groups')
    total_price = models.IntegerField(_('총 가격'), default=0)
    discount_price = models.IntegerField(_('할인 금액'), default=0)
    payment_type = models.CharField(_('결제 방법'), choices=PAYMENT_TYPE_CHOICES, max_length=100)
    is_agreement = models.BooleanField(_('주문 동의'), default=True)

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
    code = models.CharField(_('제품 코드'), max_length=100, null=True, blank=True)
    size = models.CharField(_('사이즈'), max_length=100, null=True, blank=True)
    price = models.IntegerField(_('가격'), default=0)

    class Meta:
        verbose_name = verbose_name_plural = _('주문')
