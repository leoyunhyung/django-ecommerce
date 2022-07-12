# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class OptionGroup(Model):
    product_model = models.ForeignKey('products.ProductModel',
                                      verbose_name=_('상품 모델'),
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      blank=True,
                                      related_name='option_groups')
    name = models.CharField(_('이름'), max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _('옵션 그룹')


class Option(Model):
    option_group = models.ForeignKey('OptionGroup',
                                     verbose_name=_('옵션 그룹'),
                                     on_delete=models.CASCADE,
                                     related_name='options')
    name = models.CharField(_('이름'), max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _('옵션')

    def __str__(self):
        return '%s / %s' % (self.id, self.name)
