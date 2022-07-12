# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class ProductModel(Model):
    category = models.ForeignKey('categories.Category',
                                 verbose_name=_('카테고리'),
                                 on_delete=models.CASCADE,
                                 related_name='product_models')
    banner_image = models.ForeignKey('images.Image',
                                     verbose_name=_('배너 이미지'),
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     related_name='product_models'
                                     )
    name = models.CharField(_('이름'), max_length=100)
    release_price = models.IntegerField(_('출시가'))
    low_price = models.IntegerField(_('최저가'), null=True, blank=True)
    discount_rate = models.IntegerField(_('할인율'), null=True, blank=True)
    stock = models.TextField(_('재고'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('상품 모델')

    def __str__(self):
        return '%s / %s' % (self.id, self.name)


class ProductModelImage(Model):
    product_model = models.ForeignKey('ProductModel',
                                      verbose_name=_('상품 모델'),
                                      on_delete=models.CASCADE,
                                      related_name='product_images')
    image = models.ForeignKey('images.Image',
                              verbose_name=_('이미지'),
                              on_delete=models.CASCADE,
                              related_name='product_images')

    class Meta:
        verbose_name = verbose_name_plural = _('상품 모델 이미지')


class Product(Model):
    product_model = models.ForeignKey('ProductModel',
                                      verbose_name=_('상품 모델'),
                                      on_delete=models.CASCADE,
                                      related_name='products')
    code = models.CharField(_('제품 코드'), max_length=100, null=True, blank=True)
    price = models.IntegerField(_('가격'))

    class Meta:
        verbose_name = verbose_name_plural = _('상품')


class ProductOption(Model):
    product = models.ForeignKey('Product',
                                verbose_name=_('상품'),
                                on_delete=models.CASCADE,
                                related_name='product_options')
    option = models.ForeignKey('options.Option',
                               verbose_name=_('옵션'),
                               on_delete=models.CASCADE,
                               related_name='product_options')

    class Meta:
        verbose_name = verbose_name_plural = _('상품 옵션')
