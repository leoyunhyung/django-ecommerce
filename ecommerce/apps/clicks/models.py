# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class ProductModelClick(Model):
    user = models.ForeignKey('users.User',
                             verbose_name=_('유저'),
                             on_delete=models.CASCADE,
                             related_name='product_model_clicks')
    product_model = models.ForeignKey('products.ProductModel',
                                      verbose_name=_('상품 모델'),
                                      on_delete=models.CASCADE,
                                      related_name='product_model_clicks')

    class Meta:
        verbose_name = verbose_name_plural = _('상품 모델 클릭')
