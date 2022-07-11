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
                                     verbose_name=_('이미지'),
                                     on_delete=models.CASCADE,
                                     related_name='product_models')
    name = models.CharField(_('이름'), max_length=100)
    release_price = models.IntegerField(_('출시 가격'))

    class Meta:
        verbose_name = verbose_name_plural = _('상품 모델')


class ProductModelImage(Model):
    product_model = models.ForeignKey('ProductModel',
                                      verbose_name=_('상품 모델'),
                                      on_delete=models.CASCADE,
                                      related_name='product_images')
    image = models.ForeignKey('images.Image',
                              verbose_name=_('이미지'),
                              on_delete=models.CASCADE,
                              related_name='product_images')
    code = models.CharField(_('이름'), max_length=100)
    price = models.IntegerField(_('가격'))

    class Meta:
        verbose_name = verbose_name_plural = _('상품 모델 이미지')


class Product(Model):
    product_model = models.ForeignKey('ProductModel',
                                      verbose_name=_('상품 모델'),
                                      on_delete=models.CASCADE,
                                      related_name='products')
    name = models.CharField(_('이름'), max_length=100)

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
