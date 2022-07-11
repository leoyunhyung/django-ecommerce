# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model
from ecommerce.modules.choices import QUESTION_TYPE_CHOICES


class Inquiry(Model):
    user = models.ForeignKey('users.User',
                             verbose_name=_('유저'),
                             on_delete=models.CASCADE,
                             related_name='questions')
    product_model = models.ForeignKey('products.ProductModel',
                                      verbose_name=_('상품 모델'),
                                      on_delete=models.CASCADE,
                                      related_name='questions')
    type = models.CharField(_('유형'), max_length=100, choices=QUESTION_TYPE_CHOICES)
    content = models.CharField(_('내용'), max_length=500)

    class Meta:
        verbose_name = verbose_name_plural = _('문의')
